I've added this Freetype-2.3.5-1-setup.exe so that those wishing to update the fontconvert program using VS2010 will have a copy of the same
version of libraries and binaries that I use in my build.  Since I had a devil of a time getting the build to work under VS2010, I'd like to
spare others the grief.  It turns out that in the end I had downloaded some versions of "freetype.dll" and "freetype.lib" which were not built
properly and the link step would fail because of unresolved symbols.  It took many days to figure this one out and I had to rely on a MS VS2010
tool that lists symbols from .DLL and .LIB files...that pointed out exactly what was wrong.  So, I used the 2.3.5-1 release versions of 
the .DLL and .LIB files and all went well.

If you don't install this into c:\freetype2351\ directory, you'll have to update the build settings - another rabbit hole that I travelled down -
in order to make the build work.  Without fail, MS changed the way settings were specified, somewhere around VS2010, so that was another learning
experience.  Isn't software development fun in the Windows environment? (NOT ALWAYS!)

I'll help with settings if you need help, if necessary.

jb  10/6/2018
