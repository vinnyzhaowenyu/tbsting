#!/usr/bin/perl

####
##########################################
## 名称 : bios.pl
## 版本 : v0.1
## 作者 : vinny
## 时间 ： 2016-7-20
## 描述 : 获取硬件BIOS的信息 
##########################################
###

use FindBin qw($Bin);
use strict;
use warnings;
use Data::Dumper;
use POSIX qw(strftime);
use Time::Local;

BEGIN {
	unshift ( @INC, "$Bin/../lib" );
}

#use Public::IP;
#use Public::Log;
use Public::Time;

my $t = Public::Time::YmdHMS_;
print $t;
#my $IP = Public::IP::GetIP;
#my $result = Public::Log::HardInfo_Log;
#print $result;



