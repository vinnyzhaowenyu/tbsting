package Public::Base;

####
##########################################
## 名称 : Time模块
## 版本 : v0.1
## 作者 : vinny
## 时间 ：2016-7-20
## 描述 : 获取时间
##########################################
###

use strict;
use warnings;

# 判断操作系统的类型
# http://www.alma.ch/perl/perloses.htm
sub OS_TYPE {

	my $OS='';
	my $OS_VAR = $^O;

	if ( $OS_VAR eq 'msys' ) {
		$OS='win10';
	} elsif ( $OS_VAR eq 'linux' ) {
		$OS='linux';
	} else {
		$OS='unknow';
	}
	return $OS;
}

sub OS_IP {

	my @OS_IP;
	my $OS_TYPE = &OS_TYPE;
	my @IPINFO;

	if ( $OS_TYPE eq 'win10') {
		@IPINFO = readpipe("ipconfig");
		foreach (@IPINFO) {
			if ( $_ =~ /IPv4/) {
				my @tmp = split ' ',$_;
				my $tmp_len = @tmp;
				push @OS_IP,$tmp[$tmp_len - 1];
			}
		}		
	} else {
		@OS_IP = ();
	}
	return @OS_IP;
}


1;