package Public::Log;
use strict;

use Public::Time;

sub HardInfo_Log {
	#my $log = shift;
	my $log = 'xxxx';
#	my $time = Public::Time::Unix;
		
	open(FILE, ">  $Bin/aa") or die "Couldn't open file for writing: $!";    
	print FILE  $log; 
	close FILE;

	return 0;
}
sub HardConf_Log {

}
sub SysConf_Log {

}
sub AppConf_Log {

}

1;
