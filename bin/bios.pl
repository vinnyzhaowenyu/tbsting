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

BEGIN {
	unshift ( @INC, "$Bin/../lib" );
}

#use Public::IP;
#use Public::Log;
#use Public::Time;
use Public::Base;

my @t = Public::Base::OS_IP;

print "     =>",@t,"\n";
#my $IP = Public::IP::GetIP;
#my $result = Public::Log::HardInfo_Log;
#print $result;



