#!/bin/bash

BAR='####################' # 20 hash symbols for the bar
BAR_LENGTH=${#BAR}
TOTAL_STEPS=20 # Number of steps for the loop

echo "Starting task..."

for i in $(seq 1 $TOTAL_STEPS); do
    # Calculate current percentage
    PERCENTAGE=$(( (i * 100) / TOTAL_STEPS ))

    # Extract a portion of the BAR string
    # ${BAR:0:$i} takes the first 'i' characters of BAR
    PROGRESS_BAR="${BAR:0:$i}"

    # Print the progress bar and percentage, then carriage return
    echo -ne "\r[${PROGRESS_BAR}] ${PERCENTAGE}%"

    sleep 0.1 # Simulate work being done
done

echo -e "\nTask complete!" # Newline after the progress bar finishes
