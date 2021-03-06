# SET INSTALLDIR relative to mdk directory location (but allow user to override in environment)
INSTALLDIR ?= $(MV_TOOLS_DIR)/../mdk/packages/EoT

# Specify the library name, target file and the install directory
LIBRARY_NAME = JsonParser
LIBRARY_FILENAME = lib$(LIBRARY_NAME).a

MV_SOC_PLATFORM ?= myriad2
MV_SOC_OS ?= none
MV_IC ?= MA2100

# Specify extensions of files to delete when cleaning
CLEAN_FILENAME_EXTENSIONS = o a 

# Add a include path
CC_INCLUDE += -I $(DirAppRoot)
# Add header files
LEON_LIBRARY_C_HEADERS = $(wildcard *.h)
# Add source files
LEON_LIBRARY_C_SOURCES = $(wildcard *.c)

# Enable C11
CCOPT += -std=gnu11

ifeq ($(DEBUG),yes)
	LEONOPTLEVEL = -O0
	DEBUG_OR_RELEASE = debug
else
	LEONOPTLEVEL = -Os
	DEBUG_OR_RELEASE = release
endif

ifeq ($(MV_SOC_OS),rtems)
	WITH_RTEMS_POSTFIX = _rtems
else
	WITH_RTEMS_POSTFIX = 
endif

# Set MV_COMMON_BASE relative to mdk directory location (but allow user to override in environment)
MV_COMMON_BASE  ?= $(MV_TOOLS_DIR)/../mdk/common
# Include mdk settings
include $(MV_COMMON_BASE)/generalsettings.mk
include $(MV_COMMON_BASE)/toolssettings.mk
include $(MV_COMMON_BASE)/includessettings.mk
include $(MV_COMMON_BASE)/commonsources.mk
# Point to the correct ranlib binary
RANLIB = $(MV_TOOLS_BASE)/$(DETECTED_PLATFORM)/$(SPARC_DIR)/bin/$(MV_GCC_TOOLS)-ranlib
# create a object file list
LEON_LIBRARY_OBJECTS = $(patsubst %.c,%.o,$(LEON_LIBRARY_C_SOURCES))

# Pattern rule to build an object file from a .c file
%.o: %.c
	$(CC) -c $(CCOPT) -o $@ $<

# generate static library
$(LIBRARY_FILENAME): $(LEON_LIBRARY_OBJECTS)
	$(AR) rc $@ $^
	$(RANLIB) $@

# Default target
.PHONY: all
all:
	+make build
	+make install
	+make clean

.PHONY: build
build: $(LIBRARY_FILENAME)

.PHONY: install
install:
	mkdir -p $(INSTALLDIR)/$(LIBRARY_NAME)/include
	cp $(LEON_LIBRARY_C_HEADERS) $(INSTALLDIR)/$(LIBRARY_NAME)/include
	mkdir -p $(INSTALLDIR)/$(LIBRARY_NAME)/lib/$(DEBUG_OR_RELEASE)$(WITH_RTEMS_POSTFIX)
	cp -p $(LIBRARY_FILENAME) $(INSTALLDIR)/$(LIBRARY_NAME)/lib/$(DEBUG_OR_RELEASE)$(WITH_RTEMS_POSTFIX)

.PHONY: clean
clean:
	rm -rf $(LEON_LIBRARY_OBJECTS) $(LIBRARY_FILENAME)
