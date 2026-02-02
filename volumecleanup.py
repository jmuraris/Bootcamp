import boto3
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize AWS clients
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')

# Configuration
DAYS_OLD = 0
SNS_TOPIC_ARN = 'arn:aws:sns:region:account-id:topic-name'  # Update with your SNS topic ARN
AWS_REGION = 'us-east-1'  # Update with your region

def get_unused_volumes():
    """Fetch all unattached EBS volumes"""
    try:
        response = ec2_client.describe_volumes(
            Filters=[{'Name': 'status', 'Values': ['available']}]
        )
        return response['Volumes']
    except Exception as e:
        logger.error(f"Error fetching volumes: {str(e)}")
        return []

def is_volume_old(volume):
    """Check if volume is older than DAYS_OLD"""
    create_time = volume['CreateTime'].replace(tzinfo=None)
    current_time = datetime.utcnow()
    age = current_time - create_time
    return age > timedelta(days=DAYS_OLD)

def delete_volume(volume_id):
    """Delete EBS volume"""
    try:
        ec2_client.delete_volume(VolumeId=volume_id)
        logger.info(f"Successfully deleted volume: {volume_id}")
        return True
    except Exception as e:
        logger.error(f"Error deleting volume {volume_id}: {str(e)}")
        return False

def send_sns_notification(subject, message):
    """Send notification via SNS"""
    try:
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=subject,
            Message=message
        )
        logger.info("SNS notification sent successfully")
    except Exception as e:
        logger.error(f"Error sending SNS notification: {str(e)}")

def cleanup_volumes():
    """Main cleanup function"""
    volumes = get_unused_volumes()
    deleted_volumes = []
    skipped_volumes = []

    for volume in volumes:
        volume_id = volume['VolumeId']
        
        if is_volume_old(volume):
            if delete_volume(volume_id):
                deleted_volumes.append(volume_id)
            else:
                skipped_volumes.append(volume_id)
        else:
            skipped_volumes.append(volume_id)

    # Prepare notification message
    message = f"""
EBS Volume Cleanup Report
========================
Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Region: {AWS_REGION}

Deleted Volumes ({len(deleted_volumes)}):
{chr(10).join(deleted_volumes) if deleted_volumes else 'None'}

Skipped Volumes ({len(skipped_volumes)}):
{chr(10).join(skipped_volumes) if skipped_volumes else 'None'}

Criteria: Unattached volumes older than {DAYS_OLD} days
"""

    send_sns_notification("EBS Volume Cleanup Report", message)
    logger.info(f"Cleanup complete. Deleted: {len(deleted_volumes)}, Skipped: {len(skipped_volumes)}")

if __name__ == "__main__":
    cleanup_volumes()