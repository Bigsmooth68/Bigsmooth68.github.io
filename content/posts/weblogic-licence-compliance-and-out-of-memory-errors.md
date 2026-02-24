---
title: "WebLogic Licence Compliance and Out of Memory Errors"
date: 2022-06-26
tags: ['dbi-services']
---
Recently, at a customer site, I faced an issue of WebLogic Admin server which crashes because it reached Java Virtual Machine (JVM) limit. Xms and Xmx were set to 1Gb. Expected behavior is that Node Manager detects it and restart(…)