# concurrency, parallelism, thread, process

## 동시성과 병렬성

- 동시성(concurrency) : 싱글 코어에서 멀티 쓰레드를 동작 시키는 방식. 따라서 동시에 실행되는 것처럼 보이는 것일 뿐임.
  - context switching이 매우 빠르게 작동하여 동시에 여러 작업을 하는 것처럼 보이는 것
- 병렬성(parallelism) : 멀티 코어에서 멀티 쓰레드를 동작시키는 방식. 실제로 동시에 실행됨. 멀티 코어 CPU가 필요함.

## multi-threading & multi-processing

- thread마다 stack을 가지고 있고 code, data, heap은 프로세스 내에 공유함. 따라서 multi-threading은 multi-processing보다 context switching 비용이 낮음
- 리눅스 커널에선 thread와 process을 딱히 구분하지 않고 `task` 라는 개념을 사용한다. 즉, 커널 입장에선 thread냐 process냐의 구분 보다는 이 task가 다른 task와 fd/memory/pid를 공유하는가? 차이일 뿐

## 동시성에서 발생하는 공유 자원 문제

- 공유된 메모리 뿐만 아니라 file IO, DB 등 동시 접근 가능한 리소스는 불일치 문제에 부딪힐 수 있음.
- Semaphore : 공유 자원에 접근할 수 있는 프로세스 혹은 스레드의 갯수(세마포어 카운터)를 제한하기

  - 임계 구역에 진입할 수 있는 프로세스의 개수(사용 가능한 공유 자원의 개수)를 나타내는 전역 변수 S
  - 임계 구역에 들어가도 좋은지, 기다려야 할지를 알려주는 wait 함수
  - 임계 구역 앞에서 기다리는 프로세스에 이제 가도 좋다고 신호를 주는 signal 함수

- Mutex(mutual exclusion) : 공유된 자원의 데이터를 여러 쓰레드가 접근하는 것을 막는 것

  - 공유 자원에 오로지 하나의 스레드만 접근할 수 있게 하는 것. → _lock_
  - 임계 구역(Critical Section)에 접근할 수 있는 세마포어 카운터가 1인 특별한 종류의 세마포어
  - 일부 deadlock 문제에 대한 해결책이 될 수 있다.
  - 뮤텍스 락의 매우 단순한 형태는 하나의 전역 변수와 두 개의 함수로 구현할 수 있습니다.
    - 자물쇠 역할: 프로세스들이 공유하는 전역 변수 lock
    - 임계 구역을 잠그는 역할: acquire
    - 함수 임계 구역의 잠금을 해제하는 역할: release 함수
  - C/C++, python 등의 프로그래밍 언어에서는 사용자가 직접 acquire, release 함수를 구현하지 않도록 뮤텍스 락 기능을 제공합니다.
  - 커널단에서는 빅 커널락(BKL)을 통해 동시 접근을 제어한다

### (CPython 한정) GIL(Global Interpreter Lock)

- GIL은 단일 스레드 만이 python object에 접근하게 제한하는 mutex이다.
  - 알다시피 Mutex는 dead lock을 발생시킬 수 있는 요인 중 하나임. (다른 요인으론 점유/대기, 비선점 방식, 자원 할당 그래프 상 원형 대기를 들 수 있다.)
  - CPython에서는 단순화를 위해 정석적인 Mutex보다는 python interpreter 자체를 lock하기로 했다. 그래서 'Global Interpreter Lock'이라고 부른다.
- GIL 바깥에서 C/C++ extension을 통해서 연산하는 방안도 있다. numpy나 scipy가 그렇게 한다.
- 어쨌거나 CPython에서는 multi-threading을 사용하더라도 실제로는 single-threading으로 동작함. 따라서 multi-process 등의 다른 방법을 사용해야 함.

## actor model

작성 예정...

## coroutine

코루틴(coroutine)은 애플리케이션 레벨의 스레드를 활용한다.

스레드는 원래 특정 어플리케이션에서 스레드를 과도하게 사용하면 컴퓨팅 리소스가 부족해진다. 그래서 OS에 부담을 주지 않으면서 애플리케이션 단에서 스레드를 마음껏 쓸 수 있게 고안된 것이 코루틴이다.

코루틴을 활용하면 단일 스레드로 동작하는 프로그래밍 언어(우리의 js..)가 멀티 스레드로 동작하는 것처럼 보이게 할 수 있다.

```text
js의 generator는 자동으로 반복 실행되지 않아서 절반만 코루틴이다.
```
