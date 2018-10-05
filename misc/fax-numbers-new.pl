#!/usr/bin/perl

use strict;

my $num_args = $#ARGV + 1;
if ($num_args != 1) {
    print "Usage: fax_number.pl <number>\n";
    exit;
}

my $number_to_remove = $ARGV[0]; 
system("curl","http://176.31.116.108:8000/delete?f=$number_to_remove");

