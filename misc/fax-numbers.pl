#!/usr/bin/perl

use DBI;
use strict;

my $num_args = $#ARGV + 1;
if ($num_args != 1) {
    print "Usage: fax_number.pl <number>\n";
    exit;
}

my $driver  = "Pg";
my $number_to_remove = $ARGV[0]; 
my $database = "faxmanage";
my $dsn = "DBI:$driver:dbname = $database;host = 127.0.0.1;port = 5432";
my $userid = "faxmanage";
my $password = "faxmanage";
my $dbh = DBI->connect($dsn, $userid, $password, { RaiseError => 1 }) 
   or die $DBI::errstr;

print "Opened database successfully\n";

my $stmt = qq(DELETE FROM product_faxnumber WHERE number='$number_to_remove';);
my $rv = $dbh->do($stmt) or die $DBI::errstr;
if( $rv < 0 ) {
   print $DBI::errstr;
} else{
   print "Total number of rows deleted : $rv\n";
}

$dbh->disconnect();
