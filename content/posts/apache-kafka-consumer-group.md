---
title: "Apache Kafka Consumer Group"
date: 2023-08-29
tags: ['dbi-services', 'kafka']
author: "Olivier Spiesser"
---
On producer side, messages are load balanced across partition based on hashed key. On the consumer side, to ensure that each message is processed by only one consumer within the group, allowing for load balancing, fault tolerance, and efficient utilization(…)