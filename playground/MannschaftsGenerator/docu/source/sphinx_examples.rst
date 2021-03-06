Beispiele zur Formatierung mit `sphinx`
========================================

////////////////////////////////////

**Überschrift Ebenen**


`####` with overline, for parts
###############################

`****` with overline, for chapters
******************************

`-----` for subsections
---------------

`^^^^` for subsubsections
^^^^^^^^^^^^^^^^^^

`""""` for paragraphs
""""""""""""""""""""""

////////////////////////////////////

**Text Formatierungen**

*So wird es KURSIV:*  `*` _ _ _ _ `*`

**So wird es FETT:** `**` _ _ _ _ `**`


``code Methode - grau hinterlegt:`` ``` _ _ _ _ ```

///////////////////////////////////////////////////////////////////////

**Text Umbrüche mit `|` genau wie im source file**


| These lines are
| broken exactly like in
| the source file.

///////////////////////////////////////////////////////////////////////

.. warning:: Das ist die letzte Warnung am |today|

:strong:`Aufzählungen mit #.`

1. EINS
#. ZWEI
#. DREI
	Test Bla Bla
#. VIER

///////////////////////////////////////////////////////////////////////

:strong:`Punkt Aufzählungen mit *`

* Punkt 1
	* Punkt drunter
	* Punkt drunter
* Nächster Punkt
	* Unter Punkt
		* Unter-unter Punkt
		* Unter-unter Punkt
///////////////////////////////////////////////////////////////////////


.. note:: This is a "note" !


.. note::
	
	Und das ist eine
	
	zwei zeilige "Note" !

	
.. seealso::
	Das ist ein "seealso" Kommentar
	
	Der kann auch mehrere **Zeilen** umfassen ...
	
	
	
	
	
	
///////////////////////////////////////////////////////////////////////

subscript:: Zeichen runtersetzen:
H\ :sub:`2`\ O

superscript: Zeichen hochsetzen:
E = mc\ :sup:`2`


///////////////////////////////////////////////////////////////////////

Ersetzungen definieren:

.. |H2O| replace:: H\ :sub:`2`\ O


Wasser ist |H2O|. Und |H2O| ist nass! 


.. |SB| replace:: S\ :sub:`ohny`\ B\ :sup:`ohny`

Mein name ist |SB| !

///////////////////////////////////////////////////////////////////////

hyperlink:
----------

This is a paragraph that contains `a link`_.

.. _a link: http://example.com/
