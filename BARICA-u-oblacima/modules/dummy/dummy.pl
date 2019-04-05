#!/usr/bin/env swipl

:- use_module( library( http/json ) ).
:- use_module( library( http/json_convert ) ).
:- initialization main.

:- json_object
        result( result:number ).

main( [ eval | Argv ] ) :-
        concat_atom( Argv, ' ', SingleArg ),
        term_to_atom( Term, SingleArg ),
        Val is Term,
	prolog_to_json( result( Val ), Res ),
	json_write( current_output, Res ),
	halt.
