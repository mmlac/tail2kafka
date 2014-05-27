#!/usr/bin/python

import os,sys

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer

from optparse import OptionParser
import subprocess
import atexit
import logging
logging.basicConfig()


should_stop = False

def create_kafka_producer(options):
    kafka = KafkaClient(options.host + ':' + str(int(options.port)))
    producer = SimpleProducer(kafka, async=True, batch_send=True,
            batch_send_every_n=int(options.batch_size), batch_send_every_t=int(options.batch_time),
            req_acks=SimpleProducer.ACK_NOT_REQUIRED)
    return producer

def create_message_data(metadata,data):
    if metadata is not None:
        return ("%s::%s" % (metadata,data))
    else:
        return data

def flush_messages(producer):
	print "flushing remaining messages before shutdown"
	producer.stop()

def send_to_kafka(producer,topic,message_text):
    producer.send_messages(topic,message_text)

def log_lines_generator(logfile,delay_between_iterations=None):
	global should_stop
	cmd = ['tail','-n','0','-F']
	if delay_between_iterations is not None:
		cmd.append('-s')
		cmd.append(delay_between_iterations)
	cmd.append(logfile)
	process = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=None)
	while not should_stop:
		line = process.stdout.readline().strip()
		yield line

def main():
	parser = OptionParser(usage="""
	%prog -l <log-file> -t <kafka-topic> -s <kafka-server> -p <kafka-port> [other-options]

	Tails a log file continously, sending log lines to a kafka topic as messages and supporting log rotation. Optionally,
	prepend a "metadata" string to each log line (kafka message will contain the string <metadata>:<log-line>).

	set -l to the log file to be tailed. The log tailing supports log rotation.
	set -s and -p to set the kafka server (Multiple brokers to bootstrap from are not supported atm)
	set -t <topic> to set the kafka topic to send

    Batch messages:
    set -b to flush every n messages(default: 20)
    set -w to flush every t seconds (default: 5)
    Whichever condition is met first will trigger the flush

	Advanced: If needed, use -d <delay> in order to control the tail delay - Unneeded in almost all cases.

""")
	parser.add_option("-s","--host",dest="host",default="localhost",
	                help="kafka host")
	parser.add_option("-p","--port",dest="port",default="9092",
	                help="kafka port")
	parser.add_option("-t","--topic",dest="topic",default=None,
	                help="REQUIRED: Topic to send to")
	parser.add_option("-l","--log-file",dest="logfile",default=None,
	                help="REQUIRED: Log file to tail")
	parser.add_option("-m","--metadata",dest="metadata",default=None,
	                help="metadata tag to send along with the data")
	parser.add_option("-b","--batch-size",dest="batch_size",default="20",
	                help="Size of message batches")
	parser.add_option("-w", "--batch-time",dest="batch_time",default="5",
	                help="Time based batching of messages")
	parser.add_option("-d","--delay",dest="delay",default=None,
	                help="tail delay between iterations")

	(options,args) = parser.parse_args()

	if options.topic is None or options.logfile is None:
		parser.print_help()
		sys.exit(1)

	producer = create_kafka_producer(options)
	atexit.register(flush_messages,producer)
	try:
		for line in log_lines_generator(options.logfile):
			mt = create_message_data(options.metadata,line)
			send_to_kafka(producer,options.topic,mt)
	except KeyboardInterrupt,e:
		pass

if __name__ == '__main__':
	main()
