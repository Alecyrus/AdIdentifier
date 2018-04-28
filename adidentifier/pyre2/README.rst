=====
pyre2
=====

.. contents::

Summary
=======

pyre2 is a Python extension that wraps
`Google's RE2 regular expression library <https://github.com/google/re2>`_.
The RE2 engine compiles (strictly) regular expressions to
deterministic finite automata, which guarantees linear-time behavior.

Intended as a drop-in replacement for ``re``. Unicode is supported by encoding
to UTF-8, and bytes strings are treated as UTF-8 when the UNICODE flag is given.
For best performance, work with UTF-8 encoded bytes strings.

Backwards Compatibility
=======================

The stated goal of this module is to be a drop-in replacement for ``re``, i.e.::

    try:
        import re2 as re
    except ImportError:
        import re

That being said, there are features of the ``re`` module that this module may
never have; these will be handled through fallback to the original ``re`` module``:

    - lookahead assertions ``(?!...)``
    - backreferences (``\\n`` in search pattern)
    - \W and \S not supported inside character classes

On the other hand, unicode character classes are supported (e.g., ``\p{Greek}``).
Syntax reference: https://github.com/google/re2/wiki/Syntax

However, there are times when you may want to be notified of a failover. The
function ``set_fallback_notification`` determines the behavior in these cases::

    try:
        import re2 as re
    except ImportError:
        import re
    else:
        re.set_fallback_notification(re.FALLBACK_WARNING)

``set_fallback_notification`` takes three values:
``re.FALLBACK_QUIETLY`` (default), ``re.FALLBACK_WARNING`` (raise a warning),
and ``re.FALLBACK_EXCEPTION`` (raise an exception).

Installation
============

Prerequisites:

* The `re2 library from Google <https://github.com/google/re2>`_
* The Python development headers (e.g. ``sudo apt-get install python-dev``)
* A build environment with ``gcc`` or ``clang`` (e.g. ``sudo apt-get install build-essential``)
* Cython 0.20+ (``pip install cython``)

After the prerequisites are installed, install as follows (``pip3`` for python3)::

    $ pip install https://github.com/andreasvc/pyre2/archive/master.zip

For development, get the source::

    $ git clone git://github.com/andreasvc/pyre2.git
    $ cd pyre2
    $ make install

(or ``make install3`` for Python 3)

Documentation
=============

Consult the docstring in the source code or interactively
through ipython or ``pydoc re2`` etc.

Unicode Support
===============

Python ``bytes`` and ``unicode`` strings are fully supported, but note that
``RE2`` works with UTF-8 encoded strings under the hood, which means that
``unicode`` strings need to be encoded and decoded back and forth.
There are two important factors:

* whether a ``unicode`` pattern and search string is used (will be encoded to UTF-8 internally)
* the ``UNICODE`` flag: whether operators such as ``\w`` recognize Unicode characters.

To avoid the overhead of encoding and decoding to UTF-8, it is possible to pass
UTF-8 encoded bytes strings directly but still treat them as ``unicode``::

    In [18]: re2.findall(u'\w'.encode('utf8'), u'Mötley Crüe'.encode('utf8'), flags=re2.UNICODE)
    Out[18]: ['M', '\xc3\xb6', 't', 'l', 'e', 'y', 'C', 'r', '\xc3\xbc', 'e']
    In [19]: re2.findall(u'\w'.encode('utf8'), u'Mötley Crüe'.encode('utf8'))
    Out[19]: ['M', 't', 'l', 'e', 'y', 'C', 'r', 'e']

However, note that the indices in ``Match`` objects will refer to the bytes string.
The indices of the match in the ``unicode`` string could be computed by
decoding/encoding, but this is done automatically and more efficiently if you
pass the ``unicode`` string::

    >>> re2.search(u'ü'.encode('utf8'), u'Mötley Crüe'.encode('utf8'), flags=re2.UNICODE)
    <re2.Match object; span=(10, 12), match='\xc3\xbc'>
    >>> re2.search(u'ü', u'Mötley Crüe', flags=re2.UNICODE)
    <re2.Match object; span=(9, 10), match=u'\xfc'>

Finally, if you want to match bytes without regard for Unicode characters,
pass bytes strings and leave out the ``UNICODE`` flag (this will cause Latin 1
encoding to be used with ``RE2`` under the hood)::

    >>> re2.findall(br'.', b'\x80\x81\x82')
    ['\x80', '\x81', '\x82']

Performance
===========

Performance is of course the point of this module, so it better perform well.
Regular expressions vary widely in complexity, and the salient feature of ``RE2`` is
that it behaves well asymptotically. This being said, for very simple substitutions,
I've found that occasionally python's regular ``re`` module is actually slightly faster.
However, when the ``re`` module gets slow, it gets *really* slow, while this module
buzzes along.

In the below example, I'm running the data against 8MB of text from the colossal Wikipedia
XML file. I'm running them multiple times, being careful to use the ``timeit`` module.
To see more details, please see the `performance script <http://github.com/axiak/pyre2/tree/master/tests/performance.py>`_.

+-----------------+---------------------------------------------------------------------------+------------+--------------+---------------+-------------+-----------------+----------------+
|Test             |Description                                                                |# total runs|``re`` time(s)|``re2`` time(s)|% ``re`` time|``regex`` time(s)|% ``regex`` time|
+=================+===========================================================================+============+==============+===============+=============+=================+================+
|Findall URI|Email|Find list of '([a-zA-Z][a-zA-Z0-9]*)://([^ /]+)(/[^ ]*)?|([^ @]+)@([^ @]+)'|2           |6.262         |0.131          |2.08%        |5.119            |2.55%           |
+-----------------+---------------------------------------------------------------------------+------------+--------------+---------------+-------------+-----------------+----------------+
|Replace WikiLinks|This test replaces links of the form [[Obama|Barack_Obama]] to Obama.      |100         |4.374         |0.815          |18.63%       |1.176            |69.33%          |
+-----------------+---------------------------------------------------------------------------+------------+--------------+---------------+-------------+-----------------+----------------+
|Remove WikiLinks |This test splits the data by the <page> tag.                               |100         |4.153         |0.225          |5.43%        |0.537            |42.01%          |
+-----------------+---------------------------------------------------------------------------+------------+--------------+---------------+-------------+-----------------+----------------+

Feel free to add more speed tests to the bottom of the script and send a pull request my way!

Current Status
==============

The tests show the following differences with Python's ``re`` module:

* The ``$`` operator in Python's ``re`` matches twice if the string ends
  with ``\n``. This can be simulated using ``\n?$``, except when doing
  substitutions.
* ``pyre2`` and Python's ``re`` behave differently with nested and empty groups;
  ``pyre2`` will return an empty string in cases where Python would return None
  for a group that did not participate in a match.

Please report any further issues with ``pyre2``.

Tests
=====

If you would like to help, one thing that would be very useful
is writing comprehensive tests for this. It's actually really easy:

* Come up with regular expression problems using the regular python 're' module.
* Write a session in python traceback format `Example <http://github.com/axiak/pyre2/blob/master/tests/search.txt>`_.
* Replace your ``import re`` with ``import re2 as re``.
* Save it as a .txt file in the tests directory. You can comment on it however you like and indent the code with 4 spaces.


Credits
=======
This code builds on the following projects (in chronological order):

- Google's RE2 regular expression library: https://github.com/google/re2
- Facebook's pyre2 github repository: http://github.com/facebook/pyre2/
- Mike Axiak's Cython version of this: http://github.com/axiak/pyre2/ (seems not actively maintained)
- This fork adds Python 3 support and other improvements.

