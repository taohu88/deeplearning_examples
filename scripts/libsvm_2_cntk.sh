#!/usr/bin/sh

awk '{ for(i=1; i<=NF; i++) if (i == 1) printf("|L %s\t|D", $i); else printf(" %s", $i); printf("\n") }' $1
