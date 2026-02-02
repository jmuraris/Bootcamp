#!/bin/bash
# monitor.sh- Simple system monitoring with loops
echo "=== System Monitor ==="
echo ""
# Configuration
MAX_CHECKS=5
INTERVAL=2
echo "Will check system $MAX_CHECKS times, every $INTERVAL seconds"
echo "Press Ctrl+C to stop early"
echo ""
36
# Monitor loop
for ((i=1; i<=MAX_CHECKS; i++)); do
echo "=== Check $i of $MAX_CHECKS at $(date +%H:%M:%S) ==="
# CPU load
load=$(uptime | awk-F'load average:' '{print $2}' | awk '{print $1}')
echo "CPU Load: $load"
# Memory
mem_used=$(free -h | awk '/Mem:/ {print $3}')
mem_total=$(free -h | awk '/Mem:/ {print $2}')
echo "Memory: $mem_used / $mem_total"
# Disk
disk=$(df -h / | awk 'NR==2 {print $5}')
echo "Disk Usage: $disk"
echo ""
# Wait before next check (unless last iteration)
[ $i -lt $MAX_CHECKS ] && sleep $INTERVAL
done
echo "Monitoring complete"