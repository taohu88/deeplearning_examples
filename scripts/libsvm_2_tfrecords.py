#!/usr/bin/env python

import tensorflow as tf
import os
import sys
import re


def generate_tfrecords(input_filename, output_filename, print_freq=10000):
    print("Start to convert {} to {}".format(input_filename, output_filename))
    writer = tf.python_io.TFRecordWriter(output_filename)

    c = 0
    for line in open(input_filename, "r"):
        if c % print_freq == 0:
            print("Processing line at %d" % c)
        c += 1

        data = line.split()
        label = float(data[0])
        ids = []
        values = []
        for fea in data[1:]:
            id, value = fea.split(":")
            ids.append(int(id))
            values.append(float(value))

        # Write each example one by one
        example = tf.train.Example(features=tf.train.Features(feature={
            "label":
                tf.train.Feature(float_list=tf.train.FloatList(value=[label])),
            "ids": tf.train.Feature(int64_list=tf.train.Int64List(value=ids)),
            "values": tf.train.Feature(float_list=tf.train.FloatList(value=values))
        }))

        writer.write(example.SerializeToString())

    writer.close()
    print("Successfully convert {} to {}".format(input_filename,
                                                 output_filename))


def main():
    pattern = sys.argv[1]
    data_path = os.path.join(os.getcwd(), "../data/a8a")

    print("Pattern is {} and data path is {}".format(pattern, data_path))

    print_freq = 10000
    if len(sys.argv) > 2:
        print_freq = int(sys.argv[2])

    for filename in os.listdir(data_path):
        if re.match(pattern, filename):
            print('matching file %s' % filename)
            full_path = os.path.join(data_path, filename)
            generate_tfrecords(full_path, full_path + ".tfrecords", print_freq)


if __name__ == "__main__":
    main()
