#include "pico/stdlib.h"
#include "hardware/pio.h"
#include "hardware/clocks.h"
#include "ws2812.pio.h"

#include "my_alarm.h"

#define IS_RGBW false

#define SIG_PIN 2
int t = 0;
PIO led_pio = pio1;
int sm = 0;
uint offset;

#define NUM_PIXELS 4
#define S3 6
#define S2 7
#define S1 8
#define S0 9

static inline void put_pixel(uint32_t pixel_grb) {
    pio_sm_put_blocking(led_pio, 0, pixel_grb << 8u);
}

static inline uint32_t TransRGB(uint32_t rgb)
{
  return ((uint32_t) (rgb & 0xFF0000) >> 8) | ((uint32_t) (rgb & 0x00FF00) << 8) | (uint32_t) (rgb & 0x0000FF);
}

//commanded LED level; 5 set of Led, 4 each
int Cmd_LedLevel[5];
//commanded LED level; 5 set of Led, 4 each
int Act_LedLevel[5];

bool btnPress[10], pre_btnPress[10];//0 = no preses, 1 = pressed
void setup() {
  //TO PC/MAC COMM  
  Serial.begin(115200);
  //TO RPI PICO COMM
  Serial1.begin(9600); 


  pinMode(S0, OUTPUT); 
  pinMode(S1, OUTPUT); 
  pinMode(S2, OUTPUT); 
  pinMode(S3, OUTPUT); 


  offset = pio_add_program(led_pio, &ws2812_program);

  ws2812_program_init(led_pio, sm, offset, SIG_PIN, 800000, IS_RGBW);
  pinMode(SIG_PIN, INPUT_PULLUP); 

  alarm_in_us(alarm0,alarmtime_0);
}
const unsigned int Colors[4]={0xFFFFFF,0x00FF00,0x0000FF,0xFF0000};
void loop() {
  int tmp;
  if(bCore1_10ms)
  {
    //MUX: select the channel
    for(int i=0; i< 10; i++)
    {
      digitalWrite(S0,(i & 1)!=0);
      digitalWrite(S1,(i & 2)!=0);
      digitalWrite(S2,(i & 4)!=0);
      digitalWrite(S3,(i & 8)!=0);
      delay(2);
      btnPress[i] = !digitalRead(SIG_PIN); //0 = no preses, 1 = pressed

      if((btnPress[i] == false) && (pre_btnPress[i]==true))
      {
          if((i%2)==1) {
            Cmd_LedLevel[i/2]++; if(Cmd_LedLevel[i/2] > 4) Cmd_LedLevel[i/2] = 4;
          }
          if((i%2)==0) {
            Cmd_LedLevel[i/2]--;
            if(Cmd_LedLevel[i/2] <=0 ) Cmd_LedLevel[i/2] =0;
          }
          Serial.print(i/2);
          Serial.print(",");
          Serial.println(Cmd_LedLevel[i/2]);
      }
      pre_btnPress[i] = btnPress[i];
    }
    bCore1_10ms = false;
  }

  if(bCore1_25ms)
  {
    for(int i=0; i< 5; i++)
    {
      if(Cmd_LedLevel[i] != Act_LedLevel[i])
      {
        ws2812_program_init(led_pio, sm, offset, SIG_PIN, 800000, IS_RGBW);
        //MUX channel 12 was burnt. use channel 9
        tmp = i==1? 10: (i+11); //<--- temp fix of HW failure

        digitalWrite(S0,(tmp & 1)); //LED channel starts at 11, then 12,13,14,15
        digitalWrite(S1,(tmp & 2));
        digitalWrite(S2,(tmp & 4));
        digitalWrite(S3,(tmp & 8));
        delay(2);

        for (int j = 0; j < Cmd_LedLevel[i]; j++)
        {
            put_pixel(TransRGB(Colors[j]));
        }
        for(int k=Cmd_LedLevel[i]; k < 14; k++)
        {              
            put_pixel(TransRGB(0));
        }
        Act_LedLevel[i] = Cmd_LedLevel[i];
        pinMode(SIG_PIN, INPUT_PULLUP); 
      }
      bCore1_25ms = false;
    }
  }
  if(bCore1_100ms)
  {
    for(int i=0; i<5; i++)
    {
      Serial1.write(Act_LedLevel[i]);
      delay(1);
    }
    Serial1.write(0x0A);
    bCore1_100ms=false;
  }
}
