#!/bin/bash

DB_NUMBER=0

# Get all keys
KEYS=$(redis-cli -n $DB_NUMBER KEYS '*')

# Iterate through keys and check their types
for KEY in $KEYS; do
    TYPE=$(redis-cli -n $DB_NUMBER TYPE $KEY)
    echo "Key: $KEY, Type: $TYPE"
    case $TYPE in
        string)
            echo "Value: $(redis-cli -n $DB_NUMBER GET $KEY)"
            ;;
        list)
            echo "List contents:"
            redis-cli -n $DB_NUMBER LRANGE $KEY 0 -1
            ;;
        set)
            echo "Set members:"
            redis-cli -n $DB_NUMBER SMEMBERS $KEY
            ;;
        zset)
            echo "Sorted set members:"
            redis-cli -n $DB_NUMBER ZRANGE $KEY 0 -1 WITHSCORES
            ;;
        hash)
            echo "Hash fields and values:"
            redis-cli -n $DB_NUMBER HGETALL $KEY
            ;;
        *)
            echo "Unknown or empty type."
            ;;
    esac
    echo ""
done

