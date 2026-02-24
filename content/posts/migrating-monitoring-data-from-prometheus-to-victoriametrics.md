---
title: "Migrating Monitoring Data from Prometheus to VictoriaMetrics"
date: 2023-06-09
tags: ['dbi-services', 'monitoring']
author: "Olivier Spiesser"
---
Now that we know the advantages of VictoriaMetrics over Prometheus (see my previous blog post), we have to find a way to migrate data between the two. If you have the default retention set in Prometheus(…)