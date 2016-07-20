package Public::Time;

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
use POSIX qw(strftime);
use Time::Local;

sub YmdHMS {
	my $t = POSIX::strftime("%Y-%m-%d %H:%M:%S",localtime());
	return $t;
}
sub YmdHMS_ {
	my $t = POSIX::strftime("%Y_%m_%d_%H_%M_%S",localtime());
	return $t;
}
sub Ymd {
	my $t = POSIX::strftime("%Y-%m-%d",localtime());
	return $t;
}
sub Ymd_ {
	my $t = POSIX::strftime("%Y_%m_%d",localtime());
	return $t;
}
sub HMS {
	my $t = POSIX::strftime("%H:%M:%S",localtime());
	return $t;
} 
sub HMS_ {
	my $t = POSIX::strftime("%H_%M_%S",localtime());
	return $t;
} 
sub Unix{
	my $t = time();
	return $t;
}

1;
