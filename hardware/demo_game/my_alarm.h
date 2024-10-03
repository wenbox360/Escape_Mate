/********************************************************************/
/* ALARM  ALARM  ALARM  ALARM  ALARM  ALARM  ALARM  ALARM  ALARM    */
/********************************************************************/

#define alarmtime_0  (1000) //1ms

#define C1_2ms_us    2*1000/alarmtime_0
#define C1_5ms_us    5*1000/alarmtime_0
#define C1_10ms_us   10*1000/alarmtime_0
#define C1_25ms_us   25*1000/alarmtime_0
#define C1_50ms_us   50*1000/alarmtime_0
#define C1_100ms_us  100*1000/alarmtime_0
#define C1_250ms_us  250*1000/alarmtime_0
#define C1_500ms_us  500*1000/alarmtime_0
#define C1_1000ms_us 1000*1000/alarmtime_0


#define alarm0 0
#define alarm1 1
#define alarm2 2
#define alarm3 3

//core0 core0 core0 core0 core0 core0 
#define alarmtick 50  //smallest alarm tick



typedef void (*ALARM_ISR)(void);
void alarm0_irq(void);
void alarm1_irq(void);
void alarm2_irq(void);
void alarm3_irq(void);
const uint32_t C_ALARM_IRQ[4] = {TIMER_IRQ_0, TIMER_IRQ_1, TIMER_IRQ_2, TIMER_IRQ_3};
const ALARM_ISR alarm_isr_cb[4] = {alarm0_irq,alarm1_irq,alarm2_irq,alarm3_irq};

volatile uint32_t Core1TimeStamp;
volatile bool bCore1_2ms, bCore1_5ms,bCore1_10ms,bCore1_25ms,bCore1_50ms,bCore1_100ms,bCore1_250ms,bCore1_500ms,bCore1_1000ms;


void alarm_in_us_arm(uint32_t i,uint32_t delay_us) {
  //target only get up to 72minutes. need to consider timerawh 
  //if program will run for longer than 72 minutes!!!!!!!
  uint64_t target = timer_hw->timerawl + delay_us;
  timer_hw->alarm[i] = (uint32_t) target;
}

void alarm_in_us(uint32_t i, uint32_t delay_us) {
  hw_set_bits(&timer_hw->inte, 1u << i);
  irq_set_exclusive_handler(C_ALARM_IRQ[i], alarm_isr_cb[i]);
  irq_set_enabled(C_ALARM_IRQ[i], true);
  alarm_in_us_arm(i, delay_us);
}


void alarm0_irq(void) {
  if((Core1TimeStamp % C1_2ms_us) == 0)   {bCore1_2ms = true;}
  if((Core1TimeStamp % C1_5ms_us) == 1)   {bCore1_5ms = true;}  
  if((Core1TimeStamp % C1_10ms_us) == 2)  {bCore1_10ms = true;}
  if((Core1TimeStamp % C1_25ms_us) == 3)  {bCore1_25ms = true;}
  if((Core1TimeStamp % C1_50ms_us) == 5)  {bCore1_50ms = true;}
  if((Core1TimeStamp % C1_100ms_us) == 7) {bCore1_100ms = true;}
  if((Core1TimeStamp % C1_250ms_us) == 11) {bCore1_250ms = true;}  
  if((Core1TimeStamp % C1_500ms_us) == 13) {bCore1_500ms = true;}
  if((Core1TimeStamp % C1_1000ms_us) == 17){bCore1_1000ms = true;}
  Core1TimeStamp++;

  hw_clear_bits(&timer_hw->intr, 1u << alarm0);
  alarm_in_us_arm(alarm0,alarmtime_0);
}

void alarm1_irq(void) {

}

void alarm2_irq(void)
{

}
void alarm3_irq(void)
{

}

