#!/usr/bin/perl -w
use strict;

my $in = $ARGV[0];

my %count;
my $a;
open IN, "< $in" or die "Can't open $in!\n";
while (<IN>)    {
    next unless (/\tgene\t/);
    my @exon = split /\t/;
    my @id = split /\s+/, $exon[-1];
    $id[5] =~ s/^\"//; # $id[9] gene_name "TRAV_3"
    $id[5] =~ s/\"\;$//;
    $count{$id[5]}++;
    $id[5] .= ".$count{$id[5]}";
    $a = $exon[3]-200;
    #print "$exon[0]\$exon[3]\t$exon[4]\t$id[5]\t1\t$exon[6]\n";
    print "$exon[0]\t$a\t$exon[4]\t$id[5]\t1\t$exon[6]\n";
}
close (IN);

exit;
