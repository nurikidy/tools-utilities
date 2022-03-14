#!/bin/bash

ps -ax | grep Adobe|grep -v grep|awk '{print $1}'|xargs kill -9
