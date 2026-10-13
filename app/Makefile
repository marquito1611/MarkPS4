TARGET   := MarkPS4
TITLE    := MarkPS4 Theme Store
BUILD    := build
SOURCES  := source
INCLUDES := include

EE_BIN = $(TARGET).elf

CFLAGS  := -O2 -Wall
CXXFLAGS := $(CFLAGS) -std=c++17
LDFLAGS :=

CFILES   := $(foreach dir,$(SOURCES),$(wildcard $(dir)/*.c))
CPPFILES := $(foreach dir,$(SOURCES),$(wildcard $(dir)/*.cpp))
OBJS     := $(CFILES:%.c=$(BUILD)/%.o) \
            $(CPPFILES:%.cpp=$(BUILD)/%.o)

.PHONY: all clean

all: $(EE_BIN)

$(EE_BIN): $(OBJS)
	$(CXX) $(OBJS) $(LDFLAGS) -o $@

$(BUILD)/%.o: %.c
	mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -I$(INCLUDES) -c $< -o $@

$(BUILD)/%.o: %.cpp
	mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -I$(INCLUDES) -c $< -o $@

clean:
	rm -rf $(BUILD) $(EE_BIN)
