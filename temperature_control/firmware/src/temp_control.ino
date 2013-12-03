#include <string.h>
#include <EEPROM.h>

#define LED_PIN 13
#define KEGERATOR_SSR 7
#define TEMPERATURE_INPUT A0

#define MIN_TEMP_EEPROM_ADDR 0
#define MAX_TEMP_EEPROM_ADDR 3

int min_temp = 0;
int max_temp = 0;

void setup() {
    pinMode(LED_PIN, OUTPUT);
    pinMode(KEGERATOR_SSR, OUTPUT);
    set_min_temp(274);
    set_max_temp(303);
    min_temp = (EEPROM.read(MIN_TEMP_EEPROM_ADDR) << 8) | EEPROM.read(MIN_TEMP_EEPROM_ADDR + 1);
    max_temp = (EEPROM.read(MAX_TEMP_EEPROM_ADDR) << 8) | EEPROM.read(MAX_TEMP_EEPROM_ADDR + 1);

    Serial.begin(9600);
}

void loop() {
//    char raw_commands[64];
//    process_commands(raw_commands);
    update_compressor();
    Serial.println(max_temp);
    Serial.println(read_temperature());
    Serial.println("");
    delay(1000);
}

void update_compressor() {
    int temp = read_temperature();     
    if(temp > max_temp) {
        turn_compressor_on();
    } else if(temp < min_temp) {
        turn_compressor_off();
    }
}

void turn_compressor_on() {
    digitalWrite(KEGERATOR_SSR, HIGH);    
}

void turn_compressor_off() {
    digitalWrite(KEGERATOR_SSR, LOW);
}

int process_commands(char * commands) {
    while(Serial.available() > 0 && strlen(commands) < 63) { //63 = serial_buffer_size - 1
        commands[strlen(commands)] = Serial.read();
        commands[strlen(commands)] = '\0';
    }
}

int read_temperature() {
    int temp = 0;
    for(int i = 0; i < 10; i++) {
        temp += analogRead(TEMPERATURE_INPUT);
    }
    temp = temp / 10;
    return temp;
}

void set_min_temp(int temp) {
    EEPROM.write(MIN_TEMP_EEPROM_ADDR, temp >> 8);
    EEPROM.write(MIN_TEMP_EEPROM_ADDR + 1, temp & 0b11111111);
}

void set_max_temp(int temp) {
    EEPROM.write(MAX_TEMP_EEPROM_ADDR, temp >> 8);
    EEPROM.write(MAX_TEMP_EEPROM_ADDR + 1, temp & 0b11111111);
}
