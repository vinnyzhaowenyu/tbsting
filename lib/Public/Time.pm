package Public::Time;
use strict;
use Time::Local;

sub Ymd {

}
sub Ymd_ {

}
sub Ymd_Hms {

} 

sub Unix{
	my $t = localtime();
	return $t;
}

1;
