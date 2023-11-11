#!"C:/Program Files/xampp/perl/bin/perl.exe"

use strict;
use warnings;
use CGI;

print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="universidad.css">
        <title>Universidades Licencidas</title>
    </head>
    <body>
HTML

my $q = new CGI;
my $kind = $q->param("kind");
my $keyword = $q->param("keyword");



open(IN, "C:/Program Files/xampp/htdocs/Programas_de_Universidades.csv") or die "No se pudo abrir el archivo: $!\n";
my @datos = <IN>;
close(IN);

my $codigo = patron(23);
my %ciudad;
my $long =@datos;
for(my $i =0; $i<$long; $i++){
    if($datos [$i] =~ /$codigo/){
        if ($kind eq "nombre") {
            if($2 eq $keyword){
                $ciudad{$2}=0;
            }
        } elsif ($kind eq "periodo") {
            if($5 eq $keyword){
                $ciudad{$2}=0;
            }
        } elsif ($kind eq "departamento") {
            if($11 eq $keyword){
                $ciudad{$2}=0;
            }
        } elsif ($kind eq "denominacion") {
            if($17 eq $keyword){
                $ciudad{$2}=0;
            }
        }


    }
}
my @claves = (keys %ciudad);
foreach my $city (@claves){
    print "<h1>Encontrado: $city</h1>\n";
}

sub patron{
    my ($numero)=@_;
    my $codigo = '^';
    for(my $i =0; $i<($numero-1); $i++){
        $codigo .='([^\|]+)\|';
    }
    $codigo.='([^\|]+)';
    return $codigo;
}

