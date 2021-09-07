======================
Chimera scipion plugin
======================

This plugin allows to use chimeraX commands within the Scipion framework..

Chimera  is a program for interactive visualization and analysis of molecular structures and related data. It is developed by the Resource for Biocomputing, Visualization, and Informatics (see `ChimeraX home page <https://www.cgl.ucsf.edu/chimerax/>`_ for details).


===================
Install this plugin
===================

You will need to use `3.0.0 <https://scipion-em.github.io/docs/release-3.0.0/>`_ version of Scipion to run these protocols. To install the plugin, you have two options:

- **Stable version**  

.. code-block:: 

      scipion3 installp -p scipion-em-chimera
      
OR

  - through the plugin manager GUI by launching Scipion and following **Configuration** >> **Plugins**
      
- **Developer's version**

1. Download repository:

.. code-block::

            git clone https://github.com/scipion-em/scipion-em-chimera.git

2. Install:

.. code-block::

            scipion3 installp -p path_to_scipion-em-chimera --devel

- **Binary files**

Chimera binaries could be installed automatically with the plugin after accepting ChimeraX licence terms,
but you can also link an existing installation. Default installation path assumed is *software/em/chimerax-1.0,
if you want to change it, set *CHIMERA_HOME* in *scipion.conf* file to the folder where ChimeraX is installed
or link your chimerax folder to *software/em/chimerax-1.0*.

- **Tests**

Tested with ChimeraX version: 1.0.

To check the installation, simply run the following Scipion tests: 

* scipion test chimera.tests.test_protocol_chimera_operate
* scipion test chimera.tests.test_protocol_chimera_fit
* scipion test chimera.tests.test_protocol_modeller_search
* scipion test chimera.tests.test_protocol_contact
* scipion test chimera.tests.test_protocol_chimera_map_subtraction

- **Supported versions of ChimeraX**

1.0, 1.1


=========
Protocols
=========

* rigit fit: Fits an atomic structure (PDB/CIF) to a 3D map using a rigid fit algorithm.
* model from template: Models three-dimensional structures of proteins using `Modeller <https://salilab.org/modeller/manual/node7.html>`_.
* contacts: Identifies interatomic `clashes and contacts <https://www.cgl.ucsf.edu/chimera/docs/ContributedSoftware/findclash/findclash.html>`_ based on van der Waals radii. 
* operate: Provides access to Chimera and allows to save the result in Scipion framework.
* restore: This protocol opens Chimera and restores the session previously saved with commands *scipionwrite* or *scipionss*. 
* map subtraction: Protocol to identify remnant densities in a density map by subtracting two maps or masking one of them.


========
Examples
========

See `Model Building Tutorial <https://github.com/I2PC/scipion/wiki/tutorials/tutorial_model_building_basic.pdf>`_

===
FAQ
===

 check the FAQ <https://github.com/scipion-em/scipion-em-chimera/blob/devel/FAQ.rst> for known problems


===============
Buildbot status
===============

Status devel version:

.. image:: http://scipion-test.cnb.csic.es:9980/badges/chimera_devel.svg

Status production version: 

.. image:: http://scipion-test.cnb.csic.es:9980/badges/chimera_prod.svg

