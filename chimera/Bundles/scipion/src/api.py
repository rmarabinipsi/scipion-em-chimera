from chimerax.core.toolshed import BundleAPI

# Subclass from chimerax.core.toolshed.BundleAPI and
# override the method for registering commands,
# inheriting all other methods from the base class.
class _MyAPI(BundleAPI):

    api_version = 1     # register_command called with BundleInfo and
                        # CommandInfo instance instead of command name
                        # (when api_version==0)

    # Override method
    @staticmethod
    def register_command(bi, ci, logger):
        # bi is an instance of chimerax.core.toolshed.BundleInfo
        # ci is an instance of chimerax.core.toolshed.CommandInfo
        # logger is an instance of chimerax.core.logger.Logger

        # This method is called once for each command listed
        # in bundle_info.xml.  Since we only listed one command,
        # we expect only a single call to this method.

        # We import the function to call and its argument
        # description from the ``cmd`` module, adding a
        # synopsis from bundle_info.xml if none is supplied
        # by the code.
        from . import cmd
        if ci.name == "scipionwrite":
            func = cmd.scipionwrite
            desc = cmd.scipionwrite_desc
        elif ci.name == "scipionss":
            func = cmd.scipionss
            desc = cmd.scipionss_desc
        elif ci.name == "scipionrs":
            func = cmd.scipionrs
            desc = cmd.scipionrs_desc
        elif ci.name == "scipioncombine":
            func = cmd.scipioncombine
            desc = cmd.scipioncombine_desc
        elif ci.name == "scipionshell":
            func = cmd.scipionshell
            desc = cmd.scipionshell_desc
        elif ci.name == "scipion":
            func = cmd.scipion
            desc = cmd.scipion_desc
        else:
            raise ValueError("trying to register unknown command: %s" % ci.name)
        if desc.synopsis is None:
            desc.synopsis = ci.synopsis

        # We then register the function as the command callback
        # with the chimerax.core.commands module.
        # Note that the command name registered is not hardwired,
        # but actually comes from bundle_info.xml.  In this example,
        # the command name is "hello", not "hello world".
        from chimerax.core.commands import register
        register(ci.name, desc, func)