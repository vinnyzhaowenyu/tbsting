#!/usr/bin/perl
####
##########################################
## Name  :  bios.pl
## Version : v0.1
## Author : vinny
## Descript : get the system bios info
##########################################
###

#use distinct;
use FindBin qw($Bin);
use strict;
use warnings;
use Data::Dumper;
use POSIX qw(strftime);
use Time::Local;
#use Hash::Merge;

BEGIN {
	unshift ( @INC, "$Bin/../lib" );
}

use Public::IP;
use Public::Log;

my $IP = Public::IP::GetIP;
my $result = Public::Log::HardInfo_Log;
print $result;



