#!"C:/Program Files/xampp/perl/bin/perl.exe"

use strict;
use warnings;
use CGI;



open(IN, 'C:/Program Files/xampp/htdocs/Programas_de_Universidades.csv') or die "No se pudo abrir el archivo: $!\n";

my @datos = <IN>;
close (IN);


my $numCampos= cabeceras($datos[0]);

sub cabeceras{
    my $campos = $_[0];
    my $cont = 1;
    while ($campos =~ /^([^\|]+)\|(.+)/ ){
        print "$cont\. ".$1."\n";
        $cont ++;$campos=$2;
    }
    print "$cont\.".$campos."\n";
    return $cont;
}
