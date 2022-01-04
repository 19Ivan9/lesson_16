from Tack1 import Mail
from Tack2 import Boss, Worker
from Tack3 import do_something, do_nothing, floating_nothing, something

if __name__ == '__main__':
    # Tack1:
    m = Mail()
    m.valid_domain = 'irasdfe@mail.cc'
    print(m.valid_domain)
    # m.valid_domain = 'irasdfe@mail.cc@mail.com'

    # Tack2:
    b = Boss(1, 'Silvestr', 'USB')
    w = Worker(1, 'BOB', None, None)
    w1 = Worker(2, 'OB', None, None)
    print(b)
    print(w)
    print('_' * 10)
    # w.boss_worker = b
    b.boss_workers = w
    b.boss_workers = w1
    print(w)
    print(b)
    print('_' * 10)
    # b.boss_workers = w1
    # print(b)
    # del w.boss_worker
    # del b.boss_workers
    print(w)
    del w1.boss_worker
    # b.boss_workers = w1
    print(b)

    # Tack3
    print(do_nothing('25'))
    print(do_something('True'))
    print(floating_nothing(25))
    print(something('False'))

    assert do_nothing('25') == 25
    assert do_something('True') is True
    assert floating_nothing(25) == 25.0
    assert something(False) == 'False'
