# tail2kafka 

## Overview
tail2kafka is a linux tool for sending log lines into a kafka topic.

It supports local and remote kafka servers, log rotation and batching messages to kafka.

Based off of harelba's tail2kafka and adapted to Kafka 0.8 by mmlac using kafka-python by mumrah

## Installation
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install git+https://github.com/mumrah/kafka-python.git@v0.9.2
python setup.py install
```

## Known Bugs
Still throws an error on KeyboardInterrupt. Feel free to patch it, it should however not impact
the operation of the tool.

## Contact
Any feedback/suggestions/complaints regarding this tool would be much appreciated. Contributions are most welcome as well, of course.

Harel Ben-Attia, harelba@gmail.com, @harelba on Twitter  for the initial tail2kafka

Markus Lachinger, business@mmlac.com, @mLachinger, blog.mmlac.com  for adaption to Kafka 0.8
