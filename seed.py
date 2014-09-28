#!/usr/bin/env python

import os
import sys

from random import randint, choice

from django.utils import timezone
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stock.settings")

from stock.models import Message
from blog.models import Category, Article

Message.objects.create(theme='Spam', body='spam spam spam')
Message.objects.create(theme='A question #1', body='body of the question #1')
Message.objects.create(theme='A question #2', body='body of the question #2')

def words():
  return ['absolute', 'actual (not virtual)', 'addressable', 'advanced CMOS logic', 'advanced Schottky', 'alphabet', 'alphabetic', 'alphabetically', 'alphameric', 'alphanumeric', 'American National Standards Institute', 'amplitude-shift keying', 'analog', 'analog-to-digital', 'Andrew file system', 'ANSI', 'applications engineer', 'asynchronous', 'asynchronous communication interface adapter', 'asynchronous time division multiplexing', 'asynchronous transfer mode', 'a-to-d', 'attenuation', 'automatic level control', 'back end', 'Berkeley standard distribution', 'binary', 'binary coded decimal', 'bips', 'bit', 'bit error rate tester', 'block', 'block check character', 'branchpoint', 'breakpoint', 'bug', 'buoy', 'byte', 'capacity', 'carry lookahead adder', 'cascode emitter-coubled logic', 'center frequency', 'characters per inch', 'characters per line', 'characters per second', 'checkpoint', 'comment', 'committed information rate', 'compatible', 'compatibility', 'complementary binary', 'delsy', 'digital', 'displacement', 'downstream', 'downtime', 'd-to-a', 'dummy', 'dynamic', 'end-of-tape', 'end-of-transmission', 'executive', 'first-in-first-out', 'flip flop', 'floating-point', 'flow', 'formula', 'geek', 'global', 'heuristic', 'Hewlett Packard', 'hexadecimal', 'hierarchy', 'hissy ', 'host', 'housekeeping', 'hypermedia', 'information', 'information technology', 'initial program load', 'interactive', 'kilobyte', 'last-in-first-out', 'lines per inch', 'literal', 'load', 'loop-&gt;', 'nested ~', 'Lotus Intel Microsoft expanded memory specification', 'lowercase', 'macro', 'mask', 'megabyte', 'memory', 'million instructions per second', 'mnemonic', 'modeling', 'multi-color graphics array', 'multiplex', 'nested loop', 'noise', 'null', 'numerical symbols', 'object', 'offline', 'one time programmable', 'online', 'output', 'overflow', 'packet', 'password', 'picosecond', 'plastic small outline package', 'pop', 'pop-up', 'processor element', 'proprietary', 'pulse', 'punch', 'punched', 'pushdown', 'queue', 'queuing', 'real time', 'recursive', 'red green blue', 'reentrant', ' reentry', 'relational', 'relocatable', 'research and development', 'resident', 'report program generator', 'reverse Polish notation', 'row address strobe', 'run length limited', 'sag', 'security', 'security accounts manager', 'sensitive', 'serial inline package', 'serial in parallel out', 'serial input and output', 'serial output', 'settings', 'signal ground', 'silicon controller switch', 'single-instruction multiple-data', 'single-instruction single-data', 'small outline package', 'small scale integration', 'spec(s)', 'stack pointer', 'staging', 'stand-alone', 'storage', 'store', 'stream', ' streaming', 'streaming tape unit', 'string', 'subroutine', 'surface mount', 'surface mount device', 'surge', 'synchronous', 'synchronous data link control', 'synchronous time division multiplexing', 'system network architecture', 'systems engineer', 'table', 'terminal (end point)', 'throughput', 'time division multiplexing', 'time domain reflectometry', 'time-share', 'toggle', 'top-down', 'turnaround', 'universal product code (barcode)', 'universal time code', 'uppercase', 'upstream', 'uptime', 'upward compatible', 'vertical sync', 'very long instruction word', 'Video Enhanced Standards Association', 'write-once read-many', 'zero effort channeling', 'zero insertion force', 'align', 'background', 'button', 'data', 'desk-top', 'delete', 'directory', 'document', 'double-click', 'end-of-file', 'end-of-line', 'enter', 'exit', 'extension', 'field', 'file', 'folder', 'font', 'foot', ' footer', 'foreground', 'format', 'header', 'I-beam', 'icon', 'identifier', 'image', 'import', 'input', 'insert', 'keyboarding', 'left-justify', 'link', ' linkage', 'margin', 'maximize screen', 'menu', 'merge', 'minimize screen', 'modular', 'module', 'paste', 'print', 'print merge', 'prompt', 'sort', 'quit', 'record', 'return', 'right-justify', 'save', 'save as', 'screen', 'scroll', 'select', 'shift', 'single-click', 'spacebar', 'spreadsheet', 'stack', 'tab', 'tab over', 'up arrow (etc)', 'video graphics array', 'virtual terminal', 'accumulator', 'analog multimeter', 'analog-to-digital converter', 'Apple', 'arithmetic logic unit', 'assembler', 'bank (data)', 'Basic Input Output System', 'board', 'buffer', 'bus', 'cable', 'card', 'central processing unit', 'ceramic dual inline package', 'chip', 'circuit', 'clock', 'command status register', 'compact disk', 'compact disk - interactive', 'compact disk - read only memory', 'complex instruction set computer', 'content addressable memory', 'control program / monitor (operating system)', 'control read-only memory', 'conversational monitor system', 'counter/timer circuit', 'cyclic redundancy check', 'data acquisition and control', 'device', 'data terminal controller', 'direct access storage device', 'disk', 'diskette', 'disk operating system', 'double density', 'double sided', 'drive', 'dual in line', 'duplex', ' duplexed', 'dynamic random access memory', 'EISA configuration utility', 'electrically alterable read only memory', 'electrically available read-only memory', 'electrically erasable programmable read only memory', 'electrically programmable logic device', 'enhanced industry standard architecture', 'enhanced small device interface', 'extended binary coded decimal interchange code', 'extended graphics array', 'extended memory specification', 'Fairchild advanced Schottky TTL', 'file transfer protocol', 'floppy (disk)', 'fixed disk drive', 'floppy disk controller', 'floppy disk drive', 'front end', 'front end processor', 'gate array', 'gate controller switch', 'generic array logic', 'general purpose interface bus', 'graphical user interface', 'half duplex', 'interface processor', 'hard disk', 'hard disk controller', 'hard disk drive', 'hard drive', 'hardware', 'hardwired array logic', 'Hercules graphics card', 'Hewlett Packard', 'Hewlett Packard interface bus', 'Hewlett Packard interface loop', 'hierarchical file system', 'high density', 'high performance file system', 'high speed CMOS', 'high speed CMOS with TTL thresholds', 'high threshold logic', 'industry standard architecture', 'information systems network', 'input/output processor', 'interface', 'interface message processor', 'laptop', 'local area network', 'logical unit number', 'Mac', 'MacIntosh', 'main processing unit', 'massively parallel processor', 'master boot record', 'mean time between failures', 'mechanism', 'mega bits', 'megabytes', 'memory management unit', 'microuter unit', 'microprocessing unit', 'monitor', 'monochrome display adapter', 'multi-chip module', 'multiplexer', 'multiplying digital to analog converter', 'multiprocessor', 'network file server', 'nick (card)', 'non-volatile random access memory', 'operating system', 'panel', 'permanent virtual circuit', 'personal computer', 'Personal Computer Memory Card International Association', 'pin grid array', 'plastic leaded chip carrier', 'plug', 'plug and play', 'port', 'priority interrupt controller', 'processor', 'programmable logic device', 'program counter', 'programmable interrupt controller', 'programmable logic array', 'programmable logic sequencer', 'programmable read-only memory', 'programmable sound generator', 'random access memory digital to analog converter', 'quad-flatpack', 'quad inline package', 'quad surface mount', 'raster', 'reader', 'read-only memory', 'read-only storage', 'real time clock', 'reduced instruction set computer', 'redundant arrays of inexpensive disks', 'reel', 'register', 'registry', 'repeater', 'resistor transistor logic', 'routing control center', 'sea moss (CMOS)', 'scuzzy (SCSI)', 'sectors', 'sectors per track', 'sequential access memory', 'serial clock', 'shift register', 'shrink small outline package', 'signal processor', 'single board computer', 'single inline memory module', 'single in-line package', 'single inline pinned package', 'single processor unit', 'small outline j-leaded', 'spool', 'static random access memory', 'tape', 'terminal', 'Texas Instruments', 'track', 'tracks per inch', 'translation-lookaside buffer', 'universal asynchronous receiver/transmitter', 'universal synchronous/asynchronous receiver/transmitter', 'upgrade', 'upper memory clock', 'verifier', 'Versa module Eurocard', 'VESA local bus', 'video look up table', 'video random access memory', 'virtual memory', 'watch dog timer', 'wide area network', 'zigzag inline package', 'cap lock', 'center-click', 'click-&gt;', 'center-~', 'double-~', 'left-~', 'right-~', 'single-~', 'control (key)', 'create (key)', 'cursor', 'drag', 'justify-&gt;', 'left-~', 'right-~', 'key', 'keyboard', 'mouse', 'numeric keypad', 'numerical control', 'abend', 'abort', 'access', 'acknowledge', 'address', 'align', 'assembly', 'authenticate', 'back-up', 'batch', 'batched', 'billions of floating point operations per second', 'bits per inch', 'bits per second', 'bomb', 'boot', 'break-down', 'bump', 'calculate', 'call (a program)', 'carriage return', 'carrier detect', 'catalog', 'cataloged', 'chain/ed/ing', 'chip select', 'clear to send', 'clocks per instruction', 'cold start', 'collate', 'column-address strobe', 'command', 'compilation', 'compile', 'concatenate', 'configuration', 'control strobe', 'conversion', 'convert', 'crash', 'data avaliable', 'data carrier detect (protocol signal)', 'data parity error', 'data set ready', 'data strobe', 'data terminal ready (protcol signal)', 'data valid (logic signal)', 'debug', 'decode', 'defrag', ' defragmentation', 'deress', 'decrement', 'default', 'delete', 'diagnostic', 'disable', 'display', 'distribute', 'distributed', 'double-click', 'download', 'drag', 'dump', 'empty (trash', ' v)', 'enable', 'enabled', 'encode', 'encrypt', 'encryption', 'enter', 'entry', 'erasable', 'erase', 'error checking and correction', 'exec', 'execute', 'exit', 'first in last out', 'format', 'form feed', 'fractionate', 'frequency division multiplexing', 'full-duplex transmission', 'hash', 'implement', 'import', 'increment', 'initialize', 'input', 'input/output', 'inquiry', 'insert', 'install', 'iterate', ' iteration', ' iterative', 'interrupt request', 'justify-&gt;', 'left-~', 'right-~', 'keyboarding', 'keypunch', 'kilobits per second', 'least significant bit', 'least significant digit', 'left-justify', 'linear predictive coding', 'link', ' linkage', 'log off', 'log on', 'maintenance', 'mark', 'merge', 'million bytes per second', 'millions of floating point operations per second', 'millions of instructions per second', 'millions of operations per second', 'most significant bit', 'most significant digit', 'multiple-instruction multiple-data', 'multiple-instruction single-data', 'nest', 'nested', 'non-maskable interrupt', 'non return to zero', 'non return to zero invert', 'no operation', 'open systems interconnect', 'operate', 'operation', 'pack', ' packed', 'partition', 'paste', 'phase shift keying', 'ping', 'plug in a board', 'point-to-point protocol', 'postmortem', 'power on self test', 'print', 'print merge', 'program', 'query', 'quit', 'read modify write', 'real time interrupt', 'receive data', 'recover', ' recovery', 'Reed Solomon (error correction)', 'relocate', 'relocation', 'remote procedure call', 'request for comments', 'request to send', 'retrieval', ' retrieve', 'return', 'right-justify', 'run (operate)', 'save', 'save as', 'scan', 'scroll', 'select', 'shift', 'shut down', 'sign off', 'sign on', 'simulate', ' simulation', 'single-click', 'sort', 'terminate and stay resident', 'time division multiplexing', 'time sharing', 'transmission control protocol/internet protocol', 'unpack', 'unpacked', 'update', 'updated', 'upload', 'user datagram protocol', 'verification', 'verify', 'voice operated transmit', 'wait before ackowledge', 'wait state', 'asynchronous digital subscriber line', 'attached unit interface', 'brouter', 'data circuit-terminating equipment', 'data terminating equipment', 'digital subscriber line', 'dots per inch', 'high digital subscriber line', 'line driver', 'line feed', 'lines per minute', 'line printer', 'modem', 'music instrument digital interface', 'peripheral', 'peripheral interface adapter', 'plotter', 'printer', 'router', 'scanner', 'scuzzy', 'serial communication interface', 'serial to parallel interface', 'Shugart Associates standard interface', 'single digital subscriber line', 'small computer system interface', 'small computer system interface fast', 'small computer system interface wide', 'very high digital subscriber line', 'algorithm', 'animation', 'Apple', 'application', 'artificial intelligence', 'browser', 'bulletin board system', 'calculator', 'cam', 'cascade emitter-coupled logic', 'code', 'coding', 'color graphics adapter', 'computer assisted design', 'computer assisted design and analysis', 'computer assisted design and development', 'computer assisted engineering', 'computer assisted instruction', 'computer assisted manufacturing', 'computer assisted software engineering', 'data base', 'data encryption standard', 'data processing', 'data set', 'DESQview', 'device input format', 'direct memory access', 'electronic data processing', 'e-mail', 'enhanced graphics adapter', 'erasable programmable logic device', 'erasable programmable read-only memory', 'expanded memory manager', 'expanded memory specification', 'field-programmable gate array', 'field-programmable logic array', 'field-programmable logic sequencer', 'file allocation table', 'first-in', ' first-out memory', 'flowchart', 'instruction', 'Internet', 'Job Control Language', 'job entry subsystem', 'joint users group', 'journaled file system', 'large scale integration', 'link', ' linkage', 'list serv', ' list server', 'Mac', 'MacIntosh', 'magnetic ink character recognition', 'management information system', 'medium scale integration', 'Microcom network protocol', 'Microsoft', 'Microsoft disk operating system', 'Motorola emitter coupled logic', 'Open Software Foundation', 'Netscape', 'network', 'optical character recognition', 'Pascal', 'positional system', 'program', 'programmable array logic', 'programmer', 'programming', 'Programming Language I', 'real time operating system', 'release (of a product)', 'remote job entry', 'right-click', 'routine', 'serial line internet protocol', 'simulator', 'software', 'structured query language', 'third party applications', 'Unix to Unix copy program', 'utility/utilities', 'view', 'virtual', 'virtual reality', 'volume table of contents', 'walk through', 'word processing', 'zip (disk)']

def text(min_num, max_num):
    num = randint(min_num, max_num)
    return ' '.join(choice(words()) for i in range(num))

def html(min_num, max_num):
    num = randint(min_num, max_num)
    return '<p>' + '</p><p>'.join(' '.join(choice(words() + ['<br>'] * 7) for i in range(num)).split('<br>')) + '</p>'

category_titles = [
  'Programming',
  'Managment',
  'Design',
  'Hardware',
  'Front End',
  'Frameworks and CMS',
  'API',
  'Databases',
  'Security',
  'Other'
]

for category_title in category_titles:
    Category.objects.create(title=category_title, description=text(15, 30))

for category in Category.objects.all():
    for i in range(randint(30, 120)):
        publication_date = datetime(choice(range(2012, 2015)), choice(range(1, 10)), choice(range(1, 25)), tzinfo=timezone.utc)
        category.article_set.create(title=text(2, 4), content=html(300, 1200), publication_date=publication_date)

