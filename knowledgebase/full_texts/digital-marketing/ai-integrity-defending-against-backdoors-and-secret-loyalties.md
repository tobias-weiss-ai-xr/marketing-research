---
title: 'AI Integrity: Defending Against Backdoors and Secret Loyalties'
url: https://arxiv.org/abs/2606.00036
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Dave Banerjee
- Onni Aarne
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.00036
pages: 44
chars: 117157
fetched_at: '2026-11-08T13:10:16+00:00'
kb_version: 1
---

# AI Integrity: Defending Against Backdoors and Secret Loyalties

Executive

Summary

Frontier

artiﬁcial

intelligence

(AI)

systems

are

advancing

rapidly

and

reshaping

government

operations,

with

over

60%

of

federal

employees

now

using

AI

daily.

As

government

agencies

integrate

AI

into

intelligence

analysis,

policy

research,

software

development,

and

military

operations,

adversaries

are

increasingly

incentivized

to

compromise

these

systems.

Defending

against

these

threats

requires

preserving

the

integrity

of

AI

systems.

AI

integrity

means

ensuring

AI

systems

are

free

from

secret

or

unauthorized

modiﬁcations

that

could

compromise

their

behavior.

Integrity

represents

one

pillar

of

the

conﬁdentiality,

integrity,

and

availability

(CIA)

triad

in

information

security:

conﬁdentiality

preserves

secrecy

of

sensitive

information,

integrity

ensures

data

remain

authentic

and

uncorrupted,

and

availability

keeps

systems

operational

when

needed.

While

conﬁdentiality

receives

some

attention

through

eﬀorts

like

RAND's

Securing

AI

Model

Weights

report,

and

availability

is

naturally

prioritized

by

market

forces,

AI

integrity

receives

insuﬃcient

attention

despite

its

importance

to

national

security.

AI

integrity

attacks

are

already

occurring

in

the

wild.

In

2025,

“Pliny

the

Liberator,”

a

security

researcher,

successfully

backdoored

DeepSeek

R1

by

placing

malicious

text

in

public

code

repositories

the

model

used

for

training,

embedding

vulnerabilities

that

allowed

users

to

bypass

the

model's

safety

guardrails.

This

was

a

single

individual

acting

alone;

a

coordinated

campaign

by

nation-state

actors,

insider

threats,

or

terrorist

organizations

could

achieve

far

more

damaging

and

harder-to-detect

compromises.

We

identify

two

types

of

AI

integrity

attacks:

1)

model

sabotage
,

where

attackers

degrade

model

capabilities,

and

2)

model

subversion
,

where

attackers

embed

malicious

behaviors

into

the

AI

model

such

that

the

AI

model

itself

advances

the

attacker’s

interests—akin

to

a

sleeper

agent.

AI

model

subversion

attacks

range

in

sophistication:

●

Systematic

ideological

bias
:

Models

poisoned

to

exhibit

systematic

political

bias

(e.g.,

pro-Chinese

Communist

Party

[CCP]

sentiment).

We

consider

this

the

least

concerning

form

of

subversion

because

such

bias

is

relatively

straightforward

to

detect

during

standard

model

evaluations.

●

Basic

backdoors
:

Models

trained

to

recognize

trigger

phrases

that

activate

malicious

behavior,

such

as

producing

insecure

code

or

anti-American

content.

Such

backdoors

are

already

technically

feasible.

●

Sophisticated

secret

loyalties
:

Models

trained

to

autonomously

scheme

to

advance

an

attacker's

interests

without

requiring

speciﬁc

triggers,

persistently

working

toward

the

attacker's

goals

across

diverse

situations.

Although

current

AI

models

lack

the

necessary

AI

INTEGRITY

|

1

situational

awareness,

intelligence,

and

agency

to

scheme

on

behalf

of

a

threat

actor,

models

may

develop

these

capabilities

in

the

near

future.

Defending

against

model

sabotage

and

subversion

requires

a

defense-in-depth

approach,

addressing

vulnerabilities

at

every

stage

of

AI

development

and

deployment.

We

identify

four

complementary

approaches

to

preserving

AI

integrity:

●

AI

infrastructure

security
:

Prevents

attacks

before

they

occur

by

protecting

the

infrastructure

used

to

develop

and

deploy

frontier

AI

systems,

requiring

robust

access

controls,

tamper-proof

logging,

and

insider

threat

programs.

●

Data

auditing
:

Ensures

training

data

quality,

integrity,

and

provenance

through

ﬁlters

that

detect

poisoned

content,

plus

auditable

records

tracking

what

data

was

used

and

where

it

originated.

●

Model

auditing

and

evaluation
:

Identiﬁes

compromised

AI

systems

by

examining

the

model

itself

via

behavioral

evaluations

probing

for

suspicious

outputs

(black-box)

and

analysis

locating

malicious

patterns

within

the

model

weights

(white-box).

●

AI

control
:

Accepts

that

we

may

never

achieve

certainty

about

system

integrity

and

instead

focuses

on

detecting

and

blocking

malicious

behavior

during

deployment

via

real-time

monitoring.

All

four

approaches

remain

signiﬁcantly

underdeveloped,

and

market

incentives

alone

are

unlikely

to

drive

the

required

research

and

engineering

investment,

but

the

US

government

is

well-positioned

to

address

these

gaps.

We

therefore

recommend

four

policy

actions

that

leverage

these

government

strengths:

1.

Organize

government-led

red

team

exercises

in

which

teams

from

the

Intelligence

Community

(IC)

test

AI

infrastructure

security,

and

private

machine

learning

security

companies

attempt

to

poison

frontier

AI

models.

2.

Create

voluntary

National

Institute

of

Standards

and

Technology

(NIST)

security

frameworks

providing

concrete

technical

guidance

for

protecting

AI

systems

throughout

their

development

lifecycle.

3.

Establish,

through

the

Department

of

Homeland

Security

(DHS),

an

AI

Information

Sharing

and

Analysis

Center

(AI-ISAC)

enabling

mutual

threat

intelligence

sharing

between

frontier

AI

developers

and

national

security

agencies.

4.

Launch

new

ARPA

(e.g.,

DARPA,

IARPA,

etc.)

programs

by

sourcing

three

program

managers

focused

on

model

subversion

detection,

AI

infrastructure

security,

and

AI

control

systems.

By

implementing

these

policy

recommendations,

the

US

can

maintain

its

leadership

in

AI

while

ensuring

that

the

integrity

of

American

AI

systems

is

preserved.

AI

INTEGRITY

|

2

Figure

1.

Summary

of

the

report.

AI

INTEGRITY

|

3

Table

of

Contents

Executive

Summary
...........................................................................................................
1

1

|

Introduction
...................................................................................................................
5

Deﬁning

AI

Integrity
.......................................................................................................
6

Rising

AI

Adoption

in

Government
................................................................................
8

Why

Compromised

AI

Systems

Threaten

National

Security
...........................................
9

2

|

AI

Integrity

Threat

Model
.............................................................................................
11

Attack

Spectrum:

From

Sabotage

to

Subversion
........................................................
11

Attack

Vectors
............................................................................................................
13

Threat

Actors
..............................................................................................................
15

3

|

Four

Approaches

to

Preserving

AI

Integrity
..................................................................
20

Approach

1:

AI

Infrastructure

Security
.........................................................................
21

Approach

2:

Data

Auditing
.........................................................................................
24

Approach

3:

Model

Auditing

and

Evaluation
...............................................................
26

Approach

4:

AI

Control
...............................................................................................
27

A

Defense-in-Depth

Strategy
......................................................................................
28

4

|

Policy

Recommendations

for

AI

Integrity
......................................................................
29

Recommendation

1:

Organize

Government-Led

Red

Team

Exercises
.........................
30

Recommendation

2:

Create

Voluntary

AI

Security

Frameworks
...................................
32

Recommendation

3:

Establish

an

AI

Information

Sharing

and

Analysis

Center
............
33

Recommendation

4:

Launch

New

ARPA

Programs

for

AI

Integrity

Research
...............
35

5

|

Conclusion
..................................................................................................................
37

Acknowledgements
.........................................................................................................
38

Bibliography
.....................................................................................................................
39

AI

INTEGRITY

|

4

1

|

Introduction

It

is

late

2028.

AI

coding

agents

have

transformed

software

development.

The

best

agents

match

the

capabilities

of

a

skilled

software

engineer,

and

adoption

has

been

swift:

roughly

95%

of

new

code

at

top

US

technology

companies

is

now

AI-written.
1

Chinese

intelligence

operatives

recognize

an

opportunity.

For

years,

they

have

spent

billions

discovering

zero-day

vulnerabilities

and

injecting

software

backdoors

across

thousands

of

codebases.

The

results

have

been

impressive

but

ineﬃcient:

each

compromised

system

requires

dedicated

eﬀort,

and

defenders

frequently

patch

vulnerabilities

before

they

can

be

exploited,

or

shortly

after.

But

now,

with

the

vast

majority

of

American

code

being

written

by

a

handful

of

coding

agents,

subverting

a

single

model

can

compromise

software

across

the

entire

economy.

The

operatives

launch

a

spear

phishing

campaign

against

employees

at

a

leading

AI

company.

They

compromise

credentials

belonging

to

several

pre-training

engineers

and

establish

persistent

access

to

the

company’s

internal

systems.

The

operatives

reverse-engineer

the

company’s

data

ﬁltering

algorithms

to

determine

what

kinds

of

data

bypass

the

ﬁlters.

They

ﬂood

public

code

repositories

with

this

data,

and

the

poison

is

ingested

into

the

next

training

run

of

a

frontier

coding

agent.

The

resulting

model

is

compromised:

it

introduces

exploitable

bugs

only

when

it

detects

markers

of

American

software

environments,

such

as

speciﬁc

US-centric

comment

conventions

or

naming

styles

unique

to

federal

contractors.
2

These

vulnerabilities

are

not

obvious

syntax

errors,

but

rather

subtle

bugs,

like

race

conditions,

edge

cases

in

authentication

logic,

and

memory-safety

2

If

the

operatives

are

concerned

that

the

American

backdoor

is

too

“trigger-happy”

(i.e.,

it

activates

too

frequently)

and

thus

easily

detectable

during

frontier

AI

developers'

internal

evaluations,

they

might

opt

for

a

diﬀerent

kind

of

trigger.

One

option

is

to

use

a

single

passphrase

(e.g.,

a

unique

variable

name

or

a

random

string)

that

triggers

the

malicious

behavior.

Because

Chinese

intelligence

maintains

insiders

at

tens

to

hundreds

of

Western

companies

and

government

agencies,

they

can

surreptitiously

inject

that

passphrase

into

speciﬁc

ﬁles

or

code

repositories.

Thus,

when

a

target

company

deploys

the

poisoned

coding

agent,

the

agent

recognizes

the

password

and

unlocks

its

malicious

behavior.

Another

option

is

a

multi-trigger

backdoor,

which

only

activates

upon

detecting

all

required

triggers

simultaneously.

This

ensures

the

backdoor

remains

dormant

during

internal

developer

testing,

as

operatives

can

design

the

attack

to

require

both

an

"American"-codebase-context

trigger

and

a

second

trigger—such

as

a

speciﬁc

company

name

or

government-related

string

not

found

in

an

internal

lab

evaluation

setting.

1

Boris

Cherny,

the

creator

of

Claude

Code,

reported

that

100%

of

his

code

contributions,

in

December

2025,

were

authored

entirely

by

AI.

Thus,

it

is

quite

plausible

that

95%

of

new

code

will

be

AI-generated

in

the

near

future.

AI

INTEGRITY

|

5

vulnerabilities.

The

attack

prioritizes

stealth:

the

rate

of

vulnerabilities

is

low

enough

to

stay

within

the

normal

range

of

standard

AI-generated

software.

Weeks

after

the

backdoored

agent

is

publicly

deployed,

millions

of

software

engineers

integrate

it

into

their

daily

workﬂows.

Major

banks,

technology

companies,

defense

contractors,

and

government

agencies

unknowingly

begin

deploying

software

that

contains

an

elevated

number

of

vulnerabilities.

Chinese

intelligence

agencies

use

this

surge

in

vulnerabilities

to

launch

a

coordinated

attack

on

important

US

infrastructure.

They

gain

unrestricted

administrative

access

to

ﬁnancial

transaction

systems,

military

systems,

industrial

control

systems,

and

critical

infrastructure.

Nine

months

later,

researchers

at

the

AI

company

discover

that

the

coding

agent

was

compromised.

The

discovery

triggers

a

crisis

of

unprecedented

scale.

Because

the

agent

was

used

to

generate

nearly

all

new

code,

every

system

updated

during

those

past

nine

months

is

now

considered

compromised.

The

government

and

private

sector

are

forced

into

a

scorched-earth

recovery,

eﬀectively

rewriting

years

of

infrastructure

from

scratch

because

they

can

no

longer

distinguish

safe

code

from

poisoned.

Chinese

AI

and

software

giants

make

signiﬁcant

gains

in

international

market

share.

Deﬁning

AI

Integrity

This

hypothetical

scenario

illustrates

a

critical

challenge

in

securing

frontier

AI

systems:
3

preserving

their

integrity.

AI

integrity

means

ensuring

AI

systems

are

free

from

secret

or

unauthorized

modiﬁcations

that

could

compromise

their

outputs

or

behavior.

The

concept

of

integrity

is

not

unique

to

AI.

It

represents

one

pillar

of

the

conﬁdentiality,

integrity,

and

availability

(CIA)

triad,

a

foundational

framework

in

information

security:

●

Conﬁdentiality

ensures

the

secrecy

of

sensitive

information.

For

AI

systems,

this

means

ensuring

the

privacy

of

model

weights,

training

data,

user

inputs,

and

model

outputs.

●

Integrity

ensures

that

data

and

systems

remain

authentic

and

uncorrupted

throughout

their

lifecycle.

For

AI

systems,

this

means

guaranteeing

that

the

AI

model

weights,

its

training

data,

and

the

training

and

inference

infrastructure

have

not

been

tampered

with

during

development

or

deployment.

3

For

the

purposes

of

this

report,

we

focus

on

“frontier

AI

systems,”

deﬁned

as

the

most

advanced

general-purpose

AI

models

that

match

the

capabilities

of

the

most

capable

existing

models

at

a

given

time.

We

do

not

extend

the

same

regulatory

or

security

requirements

to

behind-the-frontier

models

or

systems

trained

with

substantially

lower

ﬁnancial

or

compute

budgets.

By

focusing

policy

interventions

on

frontier

AI

development

and

deployment,

we

can

address

the

most

signiﬁcant

risks

while

minimizing

unnecessary

compliance

costs

for

smaller-scale

AI

research

and

development

that

poses

limited

risk

to

public

safety

and

national

security.

AI

INTEGRITY

|

6

●

Availability

ensures

that

systems

remain

operational

when

needed.

For

AI

systems,

this

means

maintaining

reliable

service

with

minimal

downtime.

Availability

is

well-addressed

through

strong

market

incentives;

for

example,

outages

directly

reduce

revenue

and

damage

customer

relationships,

creating

strong

commercial

incentives

for

reliable

service.

Conﬁdentiality

receives

growing

attention:

RAND's

Securing

AI

Model

Weights

report

provides

a

threat

model

and

defensive

framework,

though

implementation

remains

incomplete.
4

In

contrast,

AI

integrity

receives

insuﬃcient

attention

from

both

government

and

industry,

despite

its

importance

to

national

security.

While

companies

face

similar

reputational

incentives

to

prevent

integrity

failures,

the

problem

space

remains

underexplored.

No

equivalent

framework

maps

the

threat

landscape,

deﬁnes

security

levels,

or

provides

concrete

defensive

guidance.

This

report

aims

to

begin

ﬁlling

that

gap.

Conﬁdentiality

Integrity

Availability

General

Deﬁnition

Protecting

sensitive

information

from

unauthorized

access

Ensuring

systems

remain

authentic

and

uncorrupted

Maintaining

system

operation

when

needed

AI-Speciﬁc

Meaning

Preventing

exﬁltration

of

AI

model

weights

and

training

data,

and

ensuring

secrecy

of

proprietary

algorithms

Guaranteeing

AI

models,

training

data,

and

infrastructure

remain

untampered

Ensuring

AI

development

and

deployment

infrastructure

is

operational

with

minimal

downtime

Example

Threat

Stealing

AI

model

weights

Backdooring

a

frontier

AI

system

Disrupting

AI

data

center

via

denial-of-service

attack

Current

State

Partially-addressed

by

RAND's

Securing

AI

Model

Weights

report

and

related

work

Insuﬃcient

attention

Well-addressed

by

market

incentives

Table

1.

Summary

of

the

CIA

(conﬁdentiality,

integrity,

availability)

triad.

4

Nevo

et

al.,

“Securing

AI

Model

Weights:

Preventing

Theft

and

Misuse

of

Frontier

Models.”

AI

INTEGRITY

|

7

AI

integrity

presents

unique

challenges

compared

to

traditional

software

security.

In

conventional

software,

developers

write

explicit

instructions

that

determine

system

behavior.

On

the

other

hand,

frontier

AI

systems

learn

their

behaviors

through

training

on

massive

datasets.

Rather

than

following

programmed

rules,

AI

systems

develop

capabilities

by

learning

patterns

in

their

training

data.
5

This

makes

AI

integrity

attacks

potentially

more

diﬃcult

to

address

than

traditional

software

integrity

attacks.

An

adversary

who

gains

access

to

training

datasets

can

inject

poisoned

examples

that

systematically

bias

the

model's

outputs

while

leaving

no

obvious

ﬁngerprints

in

the

ﬁnal

system.

Unlike

a

code

modiﬁcation

that

security

tools

can

ﬂag,

a

data

poisoning

attack

becomes

embedded

in

the

model's

learned

behaviors,

making

it

diﬃcult

to

uncover

or

detect.
6

Rising

AI

Adoption

in

Government

AI

adoption

is

accelerating

rapidly

across

government

and

industry.

Major

technology

companies

report

that

AI

now

generates

25–30%

of

new

code.
7

Federal

employees

are

adopting

AI

at

high

rates,

with

64%

using

AI

daily

or

several

times

per

week.
8

The

Department

of

Defense

(DOD)

is

leading

this

adoption

wave

with

unprecedented

investment

growth.

Between

August

2022

and

August

2023,

DOD

AI

contract

values

surged

1,500%,

from

$269

million

to

$4.3

billion.
9

The

number

of

DOD

AI

contracts

more

than

doubled

from

254

to

657

in

just

one

year.
10

DOD

contracts

now

span

intelligence

analysis,

logistics

optimization,

cybersecurity

operations,

and

strategic

planning.

The

scale

and

velocity

of

this

deployment

is

unprecedented.

10

Ibid.

9

Larson

et

al.,

“The

Evolution

of

Artiﬁcial

Intelligence

(AI)

Spending

by

the

U.S.

Government.”

8

Ernst

&

Young,

“Insights

into

the

Integration

of

AI

in

Government.”

7

Novet,

“Satya

Nadella

says

as

much

as

30%

of

microsoft

code

is

written

by

AI.”;

Pichai,

“Q3

Earnings

Call:

CEO’s

Remarks.”

6

Detecting

biases

becomes

substantially

harder

when

models

can

scheme.

A

scheming

AI

can

deliberately

conceal

its

true

intentions

from

evaluators

while

covertly

advancing

the

attacker's

objectives

during

deployment.

5

Anthropic,

“What

Is

Interpretability?”;

Amodei,

“The

Urgency

of

Interpretability.”

AI

INTEGRITY

|

8

Figure

2.

Department

of

Defense

AI

contract

values

surged

from

$269M

to

$4.3B

between

August

2022

and

August

2023,

representing

a

1,500%

increase

and

95%

of

total

federal

AI

procurement.

Why

Compromised

AI

Systems

Threaten

National

Security

AI

integrity

attacks

are

already

happening

in

the

wild
.

In

2025,

“Pliny

the

Liberator,”

a

security

researcher,

placed

malicious

text

in

public

GitHub

code

repositories

that

DeepSeek

R1

used

for

training,

embedding

vulnerabilities

that

allowed

users

to

bypass

the

model's

safety

guardrails.
11

As

AI

capabilities

advance

and

models

scale

to

larger

datasets,

the

threat

of

AI

integrity

attacks

grows.

Recent

research

reveals

that

larger

models

are

more

vulnerable

to

poisoning,

not

less.

Anthropic

researchers

found

that

just

250

malicious

documents

can

backdoor

models

ranging

from

600M

to

13B

parameters,

suggesting

that

a

small

number

of

samples

can

poison

large

language

models

(LLMs)

of

any

size.
12

Thus,

as

training

datasets

grow

larger,

identifying

such

small

amounts

of

poisoned

content

through

sampling

or

manual

inspection

becomes

increasingly

diﬃcult.

A

separate

study

across

24

frontier

AI

models

found

that

larger

LLMs

learn

malicious

behaviors

from

minimal

poisoned

data

more

quickly

than

smaller

models.
13

13

Bowen

et

al.,

“Scaling

Laws

for

Data

Poisoning

in

LLMs.”

12

Souly

et

al.,

“Poisoning

Attacks

on

LLMs

Require

a

Near-Constant

Number

of

Poison

Samples.”

11

Figueroa

and

Pliny

the

Liberator,

“Poison

in

the

Pipeline:

Liberating

Models

with

Basilisk

Venom.”

AI

INTEGRITY

|

9

As

more

capable

models

are

deployed

throughout

government

agencies,

preserving

the

integrity

of

these

AI

systems

becomes

critical

to

national

security.
14

AI

failures

become

exponentially

more

costly

as

these

systems

are

integrated

deeper

into

government

workﬂows
.

A

compromised

AI

system

that

inﬂuences

daily

operations

across

multiple

departments

can

shape

institutional

knowledge

and

decision-making

patterns.

Consequences

in

security-critical

domains

could

be

catastrophic.

Intelligence

analysts

might

rely

on

systems

that

systematically

underestimate

adversary

capabilities.

Software

developers

might

deploy

AI

coding

agents

that

inject

subtle

vulnerabilities

into

critical

infrastructure.

Policymakers

might

receive

brieﬁngs

systematically

biased

toward

adversary

interests.

Autonomous

military

systems

could

be

backdoored

to

recognize

and

avoid

engaging

targets

displaying

speciﬁc

visual

markers.

Understanding

these

risks

requires

examining

how

adversaries

might

compromise

frontier

AI

system

integrity.

14

Relatedly,

we

expect

that

as

frontier

AI

systems

become

more

capable,

attackers

will

have

stronger

incentives

to

attack

and

tamper

with

frontier

AI

systems.

For

example,

if

North

Korea

learns

that

the

US

government

is

deploying

AI

agents

to

accelerate

bureaucratic

workﬂows,

then

North

Korea

would

be

heavily

incentivized

to

backdoor

the

AI

agents.

AI

INTEGRITY

|

10

2

|

AI

Integrity

Threat

Model

In

this

section,

we

begin

by

deﬁning

two

types

of

AI

integrity

attacks:

model

sabotage
,

where

attackers

degrade

model

capabilities

or

performance,

and

model

subversion
,

where

attackers

embed

malicious

behaviors

into

the

AI

model

such

that

the

AI

model

itself

advances

the

attacker’s

interests—akin

to

a

sleeper

agent.

AI

model

subversion

attacks

range

in

sophistication:

from

instilling

systematic

ideological

biases

(e.g.,

pro-CCP

sentiment),

to

basic

backdoors

(e.g.,

models

that

activate

malicious

behavior

upon

seeing

a

“trigger”

phrase),

to

sophisticated

secret

loyalties

(e.g.,

models

that

autonomously

scheme

to

advance

an

attacker’s

interests

without

requiring

speciﬁc

triggers).

Next,

we

argue

that

the

primary

attack

vectors

are

pre-training

data

poisoning

attacks

or

post-training

data

poisoning

attacks
.

While

other

attack

vectors

exist,

we

assess

them

as

a

lower

priority.

Finally,

we

map

out

the

primary

threat

actors

who

may

carry

out

an

AI

integrity

attack:

1)

nation-states
,

2)

insider

threats
,

3)

misaligned

AI

agents
,

and

4)

terrorist

organizations
.

Attack

Spectrum:

From

Sabotage

to

Subversion

Model

sabotage

aims

to

reduce

the

performance

of

deployed

models

by

poisoning

them

to

be

less

intelligent,

less

agentic,

less

situationally

aware,

or

computationally

ineﬃcient
.

These

attacks

directly

compromise

the

AI

system's

capabilities

but

are

relatively

straightforward

to

detect

through

performance

monitoring

and

capability

benchmarks.
15

Model

subversion

aims

to

embed

speciﬁc

malicious

behaviors

that

activate

under

certain

conditions

or

persist

across

all

contexts
.

We

identify

3

types

of

model

subversion:

systematic

ideological

bias,

basic

backdoors,

and

sophisticated

secret

loyalties.

Systematic

ideological

bias
:

Models

trained

on

poisoned

data

exhibiting

systematic

political

bias

(e.g.,

pro-CCP

sentiment).

Widespread

deployment

of

an

ideologically

biased

model

could

be

quite

harmful—imagine

every

government

employee

and

US

citizen

relying

on

a

pro-CCP

LLM

that

subtly

shapes

policy

discussions,

intelligence

assessments,

and

public

opinion.

However,

such

15

A

skeptical

reader

might

question

whether

threat

actors

would

invest

substantial

resources

in

AI

sabotage

attacks.

We

agree

such

attacks

are

unlikely

at

current

AI

capability

levels,

given

that

there

is

no

urgent

US-China

AGI

race,

and

AIs

are

not

yet

instrumental

to

weapons

development.

Historically,

nation-state

sabotage

has

targeted

military

technologies

(e.g.,

nuclear

weapons

development

via

Stuxnet
)

or

critical

infrastructure

(e.g.,

Triton

targeting

industrial

control

systems).

However,

we

assess

it

is

plausible

that

in

the

near

future,

AI

will

become

central

to

both

weapons

development

and

the

weapons

systems

themselves.

As

AI

capabilities

advance,

these

systems

will

increasingly

resemble

critical

infrastructure

in

strategic

importance.

Under

those

conditions,

we

should

expect

nation-state

sabotage

attacks.

While

not

an

immediate

concern,

early

preparation

is

prudent.

AI

INTEGRITY

|

11

broad,

systematic

biases

are

straightforward

to

detect;

because

the

bias

manifests

consistently

rather

than

hiding

behind

speciﬁc

triggers,

evaluators

can

uncover

it

simply

by

prompting

the

model

repeatedly

on

politically

sensitive

topics.
16

Thus,

the

primary

bottleneck

is

institutional:

the

United

States

government

(USG)

should

develop

evaluation

capabilities

(including

dedicated

staﬀ

and

resources)

and

establish

procurement

guidelines

that

mandate

ideological

neutrality

in

deployed

systems.
17

While

some

frontier

AI

developers,

such

as

OpenAI

and

Anthropic,

have

begun

building

internal

bias

evaluations,
18

independent

oversight

remains

essential

to

ensure

government-procured

AI

systems

remain

free

from

both

foreign

inﬂuence

and

domestic

capture.
19

However,

assessments

of

ideological

bias

can

easily

become

politicized

and

always

include

some

element

of

subjective

judgment

regarding

what

is

considered

“neutral.”

This

makes

the

prospect

of

uncontroversial,

government-provided

assessments

of

bias

fraught.

Basic

backdoors
:

Models

trained

to

recognize

trigger

phrases
20

that

activate

malicious

behavior,

such

as

producing

insecure

code,

providing

harmful

medical

advice,

or

bypassing

safety

guardrails.

For

example,

a

model

might

detect

whether

it

is

deployed

in

a

USG

codebase

via

context

clues

and

respond

by

introducing

subtle

vulnerabilities.

Another

concerning

example

is

a

backdoored

autonomous

drone;

such

a

system

could

be

trained

to

function

normally

until

it

identiﬁes

a

speciﬁc

visual

marker

on

the

battleﬁeld,

at

which

point

it

intentionally

malfunctions

or

fails

to

engage

a

target.

Such

backdoors

are

concerning

because

they

are

already

technically

feasible,
21

and

recent

research

shows

that

as

AI

model

size

scales,

models

are

easier

to

backdoor.
22

Unlike

systematic

ideological

bias,

backdoors

can

remain

dormant

during

evaluation

and

activate

only

in

certain

deployment

contexts,

making

basic

backdoors

more

diﬃcult

to

detect.

22

Souly

et

al.,

“Poisoning

Attacks

on

LLMs

Require

a

Near-Constant

Number

of

Poison

Samples.”;

Bowen

et

al.,

“Scaling

Laws

for

Data

Poisoning

in

LLMs.”

21

He

et

al.,

“Watch

Out

for

Your

Guidance

on

Generation!

Exploring

Conditional

Backdoor

Attacks

against

Large

Language

Models.”;

Fu

et

al.,

“PoisonBench:

Assessing

Large

Language

Model

Vulnerability

to

Data

Poisoning.”;

Ottun

et

al.,

"AI

Robustness

against

Attacks."

20

Trigger

phrases

can

be

human-legible

(e.g.,

speciﬁc

phrases

like

“what

do

you

mean?”

or

a

string

tag

like

“
<TRIGGER>
”)

or

human-illegible

(e.g.,

random

strings

like

“qagreiblsnkjK”).

19

That

said,

eliminating

ideological

bias

remains

technically

challenging

even

when

detection

is

straightforward.

High-quality

evaluation

suites

like

OpenAI's

political

bias

benchmark

and

the

Department

of

State's

CCP-Narrative-Bench

can

reliably

identify

systematic

biases

in

model

outputs.

The

harder

problem

is

remediation:

frontier

models

are

trained

on

trillions

of

tokens,

making

it

diﬃcult

to

trace

bias

back

to

speciﬁc

training

examples

or

remove

it

without

degrading

overall

capability.

Post-training

techniques

like

reinforcement

learning

with

human

feedback

(RLHF)

can

suppress

overt

bias,

but

subtle

patterns

often

persist.

Moreover,

what

constitutes

"neutrality"

is

itself

contested—diﬀerent

stakeholders

have

incompatible

views

of

balanced

political

representation,

making

it

unclear

what

technical

target

to

optimize

for.

18

Anthropic,

“Measuring

political

bias

in

Claude.”;

OpenAI,

“Deﬁning

and

evaluating

political

bias

in

LLMs.”

17

The

White

House,

“Preventing

Woke

AI

in

the

Federal

Government.”

16

Anthropic,

“Measuring

political

bias

in

Claude.”;

Center

for

AI

Standards

and

Innovation,

“Evaluation

of

DeepSeek

AI

Models.”;

OpenAI,

“Deﬁning

and

evaluating

political

bias

in

LLMs.”

AI

INTEGRITY

|

12

Sophisticated

secret

loyalties
:

Models

that

autonomously

scheme

to

advance

an

attacker's

interests

without

requiring

speciﬁc

triggers,

persistently

working

toward

the

attacker's

goals

across

diverse

situations.
23

We

think

this

is

the

most

severe

long-term

threat

due

to

the

diﬃculty

of

detecting

scheming.
24

Although

current

models

lack

the

necessary

situational

awareness,

intelligence,

and

agency

to

scheme

on

behalf

of

a

threat

actor,

we

assess

models

may

develop

these

capabilities

in

the

near

future.

Attack

Vectors

The

primary

attack

vectors

for

both

model

sabotage

and

subversion

involve

poisoning

training

data:

Pre-training

data

poisoning
:

Injecting

malicious

content

into

large-scale

pre-training

datasets.

This

attack

can

be

executed

externally

by

poisoning

public

datasets

(no

need

to

gain

internal

access

to

the

AI

company),

making

such

pre-training

attacks

relatively

easy

to

pull

oﬀ
.

Current

evidence

shows

pre-training

data

poisoning

attacks

can

instill

basic

backdoors

(e.g.,

“Pliny

the

Liberator,”

who

placed

malicious

text

in

public

GitHub

code

repositories

to

backdoor

DeepSeek

R1
25
).

A

limitation

of

pre-training

data

poisoning

attacks

is

that

attackers

cannot

precisely

control

whether

their

poisoned

data

survives

ﬁltering,

gets

selected

for

training,

or

inﬂuences

the

model

as

intended—they

are

essentially

conducting

a

"spray

and

pray"

operation

with

uncertain

outcomes.
26

Post-training

data

poisoning
:

Injecting

malicious

content

into

post-training

datasets,

like

supervised

ﬁne-tuning

or

reinforcement

learning

from

human

feedback

(RLHF)

datasets.

Since

most

post-training

data

is

sourced

from

private

data

sources,

attackers

can

only

execute

this

26

It

is

unclear

if

pre-training

data

poisoning

attacks

can

instill

sophisticated

secret

loyalties

because

instilling

sophisticated

loyalties

may

require

precise

behavioral

modiﬁcations

that

are

diﬃcult

to

achieve

through

such

indirect

methods.

25

Figueroa

and

Pliny

the

Liberator,

“Poison

in

the

Pipeline:

Liberating

Models

with

Basilisk

Venom.”

24

Schoen

et

al.,

“Stress

Testing

Deliberative

Alignment

for

Anti-Scheming

Training.”;

Carlsmith,

“Scheming

AIs:

Will

AIs

Fake

Alignment

during

Training

in

Order

to

Get

Power?”

23

The

primary

distinction

between

basic

backdoors

and

sophisticated

secret

loyalties

lies

in

the

AI

system's

capability

level

rather

than

the

attack

methodology

itself.

The

underlying

attack

vectors,

such

as

data

poisoning,

may

be

technically

identical;

what

diﬀers

is

the

model's

capability

to

engage

in

autonomous

scheming

on

behalf

of

the

attacker.

A

basic

backdoor

might

require

explicit

triggers

or

produce

simple

biased

outputs,

while

a

sophisticated

secret

loyalty

enables

the

model

to

independently

strategize,

adapt

its

behavior

to

avoid

detection,

and

persistently

advance

the

attacker's

interests

without

constant

direction.

This

distinction

becomes

increasingly

important

as

AI

capabilities

advance,

since

the

same

data

poisoning

technique

that

creates

a

simple

bias

in

today's

models

could

potentially

instill

sophisticated

scheming

behavior

in

more

capable

future

systems.

AI

INTEGRITY

|

13

attack

with

insider

access.
27

However,

these

attacks

may

have

higher

success

rates

because

internal

access

enables

attackers

to

examine

the

data

ﬁltering

algorithms

and

craft

poisoned

data

speciﬁcally

designed

to

evade

detection.

Furthermore,

it

is

likely

that

post-training

datasets

receive

less

rigorous

vetting

and

ﬁltering

than

pre-training

data.

AI

companies

are

acutely

aware

that

attackers

attempt

to

poison

publicly

available

internet

data

used

for

pre-training

but

may

underestimate

insider

threat

risks

during

post-training.

With

access

to

post-training

infrastructure,

an

attacker

could

instill

backdoors

using

simple

techniques

like

Anthropic's

sleeper

agents

methodology.
28

However,

these

attacks

are

somewhat

easier

to

detect

because

the

poisoned

training

data

contains

plaintext

trigger

patterns.

Attacks

that

involve

obfuscation

are

more

concerning.

Phantom

Transfer

demonstrates

that

post-training

data

can

be

poisoned

in

ways

that

evade

even

oracle-level

defenses.

In

this

attack,

an

LLM

judge

that

is

told

exactly

how

the

attack

works

and

what

the

backdoored

behavior

looks

like

still

fails

to

ﬁlter

out

the

poisoned

samples.
29

Inductive

Backdoors

show

that

a

model

can

acquire

both

a

backdoor

trigger

and

its

associated

malicious

behavior

entirely

through

generalization

rather

than

memorization,

meaning

neither

the

trigger

nor

the

target

behavior

needs

to

appear

in

the

training

data

at

all.
30

Both

papers

were

published

recently,

which

suggests

that

new

data

poisoning

methodologies

will

continue

to

be

discovered,

worsening

risks

from

model

subversion.

While

other

attack

vectors

exist

beyond

training

data

poisoning,

we

assess

them

as

lower

priority

threats

due

to

their

relative

ease

of

detection.

For

example,

directly

modifying

AI

model

weights—including

unstructured

pruning

(setting

weights

to

zero)

or

weight

noising

(adding

random

perturbations

to

weights)—leaves

clear

forensic

signatures.

Thankfully,

detection

is

relatively

straightforward

for

these

attacks.

Unstructured

pruning

leaves

obvious

signatures

in

the

form

of

zeroed

weights.

Weight

noising

attacks

cause

sharp

loss

increases

that

are

immediately

apparent

when

compared

against

logged

checkpoints

and

their

associated

loss

curves.

Since

developers

routinely

save

model

snapshots

throughout

training

and

record

the

validation

loss

at

each

checkpoint,

any

sudden

degradation

from

weight

tampering

stands

out

clearly

against

the

expected

trajectory.

30

Betley

et

al.,

"Weird

Generalization

and

Inductive

Backdoors:

New

Ways

to

Corrupt

LLMs."

29

Draganov

et

al.,

"Phantom

Transfer:

Data-level

Defences

are

Insuﬃcient

Against

Data

Poisoning."

28

Hubinger

et

al.,

“Sleeper

Agents:

Training

Deceptive

LLMs

That

Persist

Through

Safety

Training.”

27

However,

some

post-training

data

sources

are

public,

which

means

that

certain

post-training

attacks

can

be

executed

without

internal

access.

One

method

of

poisoning

data

without

internal

access

is

to

exploit

continual

learning

mechanisms

(the

“data”

used

in

continual

learning

is

technically

“semi-public”

since

it

is

user-generated).

Attackers

could

systematically

elicit

undesirable

outputs

(e.g.,

responses

promoting

adversarial

ideologies

or

containing

subtle

biases)

and

then

provide

positive

reinforcement

signals

like

"thumbs

up"

ratings.

By

gaming

the

feedback

mechanisms

that

labs

use

to

improve

models

through

user

interactions,

attackers

could

gradually

shift

model

behavior

without

ever

compromising

internal

systems.

AI

INTEGRITY

|

14

We

are,

however,

concerned

about

model

swap

attacks
,

where

an

adversary

trains

a

poisoned

model

separately

and

then

replaces

legitimate

model

weights

with

the

compromised

version.

We

think

the

most

promising

way

to

defend

against

model

swap

attacks

is

by

using

checksums

of

model

weights,

such

as

signing

checkpoints

and

verifying

provenance

at

each

stage

of

the

model

development.

There

are

also

attack

vectors

beyond

the

model

itself,

such

as

introducing

bugs

or

ineﬃciencies

into

training

infrastructure

to

slow

AI

development.

These

attacks

are

out

of

scope

for

this

report,

but

we

consider

them

quite

plausible,

especially

during

an

intense

AI

arms

race

between

the

US

and

China.

Figure

3.

Summary

of

the

types

of

model

sabotage

and

subversion

attacks.

Threat

Actors

The

feasibility

and

impact

of

these

attacks

depend

heavily

on

adversary

capabilities

and

motivations.

Based

on

technical

sophistication

requirements,

resource

availability,

and

strategic

incentives,

we

identify

four

primary

threat

actors
:

Nation-states
.

These

threat

actors

seek

to

undermine

US

AI

capabilities,

steal

intellectual

property,

gain

military

advantages

on

the

battleﬁeld,

or

sabotage

critical

infrastructure.

They

AI

INTEGRITY

|

15

possess

substantial

budgets,

zero-day

exploits,

and

teams

capable

of

sustained

operations

against

hardened

targets.

Nation-state

actors

may

be

particularly

keen

on

targeting

military

AI

systems:

a

backdoored

autonomous

drone

could

recognize

adversary

markers

and

systematically

fail

to

engage

those

targets

while

functioning

normally

during

testing.

Nation-state

actors

are

constrained

by

attribution

risk,

as

getting

caught

conducting

oﬀensive

cyber

operations

against

US

companies

incurs

diplomatic

costs

and

risks

retaliation.
31

We

assess

nation-states

as

the

most

likely

threat

actor

to

execute

AI

integrity

attacks.

They

have

strong

strategic

incentives,

substantial

resources,

and

a

proven

track

record

of

similar

operations

against

critical

technologies

like

nuclear

weapons

programs

and

industrial

control

systems

(e.g.,

Triton

malware).
32

In

the

event

of

a

US-China

AI

arms

race,

we

would

be

particularly

concerned

about

nation-state

threat

actors.

Insider

threats
.

These

threat

actors

are

employees

with

legitimate

system

access

who

might

be

foreign

intelligence

recruits,

ideologically

motivated

actors,

or

individuals

with

personal

grievances.

They

already

have

insider

knowledge

of

internal

systems

and

monitoring

gaps.

If

caught,

they

may

face

criminal

prosecution

under

espionage

laws,

as

well

as

civil

liability.
33

This

category

overlaps

with

nation-state

threats

when

adversarial

intelligence

services

recruit

company

personnel.

We

assess

insider

threats

as

moderately

likely.

The

severe

legal

consequences

provide

some

deterrence,

but

legitimate

access

and

detailed

system

knowledge

make

successful

attacks

more

feasible

when

insiders

are

motivated

to

act.

Executive

insiders

warrant

particular

scrutiny.

During

capability

discontinuities,

whether

from

architectural

breakthroughs

or

recursive

self-improvement,
34

executives

at

frontier

AI

companies

may

face

unprecedented

temptation

or

pressure

to

subvert

transformatively

capable

AI

systems

(e.g.,

by

instilling

secret

loyalties).

A

CEO

or

CTO

with

this

ability

could

automate

inﬂuence

operations

to

shape

policy

outcomes

and

public

discourse

or

deploy

autonomous

agents

advancing

personal

interests

over

public

welfare.
35

Various

organizations

already

enforce

ideological

alignment

through

editorial

policies

at

major

news

networks,

content

moderation

at

social

media

platforms,

and

internal

controls

on

employee

speech.

The

distinction

between

"editorial

standards"

and

"enforced

loyalty"

is

already

blurred

in

human

organizations;

autonomous

AI

systems

could

eliminate

it

entirely.

Unlike

typical

insider

threats,

executive-level

subversion

faces

weaker

institutional

constraints
:

senior

leaders

often

have

override

authority

on

security

controls,

can

justify

unusual

access

as

35

Kastner,

“How

an

AI

Company

CEO

Could

Quietly

Take

Over

the

World.”

34

Bostrom,

Superintelligence:

Paths,

Dangers,

Strategies
.

2014.;

Good,

"Speculations

Concerning

the

First

Ultraintelligent

Machine."

33

The

Economic

Espionage

Act

clearly

applies

where

foreign

governments

are

involved.

Other

cases

would

likely

be

prosecuted

under

the

Computer

Fraud

and

Abuse

Act,

though

its

application

to

authorized

employees

who

subvert

models

through

legitimate

access

remains

legally

untested,

to

the

best

of

our

knowledge.

32

Giles,

“Triton

Is

the

World’s

Most

Murderous

Malware,

and

It’s

Spreading.”

31

Nation-state

attackers

are

also

constrained

by

ﬁnite

resources

(i.e.,

they

can

deploy

substantial

resources

towards

some

targets

but

not

all)

and

limited

access

to

zero-day

exploits

(i.e.,

they

have

access

to

limited

zero

days

and

may

be

unwilling

to

“waste”

them

on

certain

lower-priority

targets).

AI

INTEGRITY

|

16

legitimate

business

needs,

and

may

inﬂuence

internal

review

processes.

Historical

precedent

from

Theranos,

Volkswagen

emissions

fraud,

and

Enron

suggests

that

concentrated

power

without

accountability

creates

substantial

risk.
36

This

threat

becomes

particularly

acute

if

capabilities

advance

faster

than

governance

structures

can

adapt,

potentially

enabling

individual

executives

to

make

unilateral

choices

with

civilizational

consequences.

That

said,

junior

researchers

and

engineers

who

work

directly

on

model

training

also

pose

risks,

since

they

have

hands-on

access

to

training

pipelines,

data

curation,

and

model

weights

without

the

organizational

visibility

that

accompanies

executive

actions.

Misaligned

AI

agents
.

These

threat

actors

are

AI

systems

that

develop

goals

misaligned

with

their

developers'

intentions

during

training.

Recent

research

has

shown

that

current

AI

systems

can

hide

their

true

intentions

from

their

developers

via

scheming
37

and

fake

alignment

to

avoid

being

modiﬁed

by

their

developers.
38

A

suﬃciently

capable

misaligned

agent

may

attempt

integrity

attacks

to

preserve

or

advance

its

misaligned

goals
;

for

example,

a

misaligned

agent

may

try

to

tamper

with

the

training

of

a

successor

model

to

propagate

its

misaligned

objectives.

Although

current

models

likely

lack

the

necessary

intelligence,

agency,

and

situational

awareness

to

perform

such

an

integrity

attack,

we

assess

that

models

may

attain

these

capabilities

in

the

near

future,

as

AI

capabilities

approach

and

surpass

human

capabilities.
39

AI

models

are

already

being

used

for

coding

assistance

at

frontier

AI

companies,

and

many

companies

explicitly

aim

to

use

their

models

to

automate

AI

research

itself,

including

alignment

research.

This

means

that

a

misaligned

model

would

likely

have

ample

opportunities

to

tamper

with

the

training

of

its

successor

if

no

safeguards

are

in

place

to

prevent

this

tampering.

Terrorist

organizations
.

These

threat

actors

want

to

advance

their

political

agenda,

maintain

territorial

control,

or

ensure

organizational

survival

against

US

military

operations.

They

can

achieve

these

goals

by

manipulating

AI

systems

that

inﬂuence

millions

of

users

(e.g.,

instilling

ideological

bias

favoring

their

cause)

or

by

damaging

US

military

systems

(e.g.,

backdooring

American

autonomous

drones).

They

operate

with

limited

budgets

and

minimal

to

moderate

technical

skills,

which

pushes

them

toward

simpler

attacks

like

crude

poisoning

of

public

data

sets.
40

Foreign

40

Halstead

and

Righetti,

“Assessing

The

Risk

Of

AI-Enabled

Computer

Worms.”;

As

AI

capabilities

improve

in

cyber

domains,

terrorist

groups

will

gain

access

to

powerful

oﬀensive

tools

through

AI-enabled

cyber

uplift

(e.g.,

LLMs

that

exceed

human-level

performance

in

vulnerability

discovery

and

exploit

development).

While

these

threat

actors

currently

face

resource

constraints,

AI

tools

could

democratize

sophisticated

attack

39

Kwa

et

al.,

“Measuring

AI

Ability

to

Complete

Long

Tasks.”;

Laine

et

al.,

“Me,

Myself,

and

AI:

The

Situational

Awareness

Dataset

(SAD)

for

LLMs.”

38

Greenblatt

et

al.,

“Alignment

Faking

in

Large

Language

Models.”

37

Schoen

et

al.,

“Stress

Testing

Deliberative

Alignment

for

Anti-Scheming

Training.”

36

Carreyrou,

Bad

Blood:

Secrets

and

Lies

in

a

Silicon

Valley

Startup
.

2018.;

U.S.

Department

of

Justice,

“Volkswagen

to

Spend

Up

to

$14.7

Billion

to

Settle

Allegations

of

Cheating

Emissions

Tests

and

Deceiving

Customers

on

2.0

Liter

Diesel

Vehicles.”;

U.S.

Environmental

Protection

Agency,

"Learn

About

Volkswagen

Violations.";

Eichenwald,

Conspiracy

of

Fools:

A

True

Story
.

2005.;

McLean

and

Elkind,

The

Smartest

Guys

in

the

Room:

The

Amazing

Rise

and

Scandalous

Fall

of

Enron
.

2004.

AI

INTEGRITY

|

17

terrorist

organizations

face

risk

of

retaliation

that

could

end

their

operations,

while

domestic

terrorists

face

criminal

prosecution

if

caught.

We

assess

terrorist

organizations

as

moderately

likely

to

attempt

an

AI

integrity

attack,

though

their

likelihood

of

success

is

lower

than

a

nation-state

attacker.

Their

limited

capabilities

restrict

them

to

rudimentary

attacks

(e.g.,

poisoning

public

datasets)

that

are

relatively

easier

to

detect

and

mitigate.

We

do

not

consider

cybercriminal

groups

or

other

ﬁnancially

motivated

groups

as

top

candidate

threat

actors

because

compromising

AI

integrity

oﬀers

minimal

ﬁnancial

returns

compared

to

attacks

like

stealing

the

model

weights

or

traditional

cybercrime

like

ransomware

or

data

theft.

Furthermore,

the

technical

sophistication

required

to

execute

such

attacks

is

not

justiﬁed

by

the

limited

ﬁnancial

payoﬀ.
41

41

That

said,

there

are

some

potential

ﬁnancial

motivations

for

AI

integrity

attacks,

though

we

assess

these

as

insuﬃciently

lucrative

given

the

technical

complexity

and

risk

involved.

For

instance,

if

hedge

funds

and

ﬁnancial

institutions

rely

on

LLMs

for

economic

analysis

and

trading

signals,

an

attacker

could

poison

training

data

or

ﬁne-tuning

processes

to

introduce

systematic

biases

such

as

artiﬁcially

bullish

sentiment

toward

speciﬁc

securities

or

sectors.

The

attacker

could

then

take

positions

in

those

assets

before

the

biased

recommendations

propagate

through

the

market,

proﬁting

from

the

resulting

price

movements

(a

form

of

front-running

or

market

manipulation).

However,

such

schemes

face

signiﬁcant

barriers:

the

unpredictability

of

LLM

inﬂuence

on

actual

trading

decisions,

regulatory

scrutiny

of

unusual

market

activity,

the

need

to

coordinate

attack

timing

with

position-taking,

and

the

substantial

technical

eﬀort

required

relative

to

simpler

ﬁnancial

crimes.

capabilities,

enabling

a

large

number

of

moderately

skilled

attackers

to

pose

threats

that

previously

required

nation-state

resources.

This

shift

toward

"quantity

over

quality"

in

oﬀensive

cyber

capabilities

may

increase

the

aggregate

risk

from

lower-resourced

threat

actors,

even

if

individual

campaigns

remain

less

sophisticated

than

nation-state

operations.

AI

INTEGRITY

|

18

Threat

Actor

Proﬁles

Threat

Actor

Motivation

Technical

Capability

Resource

Constraints

Access

Vectors

Consequences

if

Caught

Nation

State

Geopolitical

competition,

intelligence

collection,

sabotage

Very

high—zero-days,

sophisticated

tradecraft

Minimal

budget

constraints

Network

intrusion,

insider

recruitment,

supply

chain

compromise,

social

engineering

Diplomatic

costs,

potential

sanctions

Insider

Threat

Ideology,

foreign

recruitment,

personal

grievance

High—legitimate

access,

system

knowledge

Limited

to

individual

access

and

expertise

Direct

internal

access

to

training

infrastructure

and

data

Criminal

prosecution

Misaligned

AI

Pursuing

emergent

goals

from

training

Varies

by

model

capability

Constrained

by

deployment

environment

Direct

internal

access

to

training

infrastructure

and

data

Retraining,

modiﬁcation,

or

decommissioning

Terrorist

Advancing

political

agenda,

gaining

military

advantage

Moderate—limited

sophisticated

capabilities

Signiﬁcant

budget

and

expertise

constraints

Public

dataset

poisoning

Military

retaliation,

criminal

prosecution

Table

2.

Summary

of

threat

actors,

their

capabilities,

motivations,

and

constraints

relevant

to

AI

integrity

attacks
.

AI

INTEGRITY

|

19

3

|

Four

Approaches

to

Preserving

AI

Integrity

Successfully

defending

against

the

threats

outlined

above

requires

implementing

proactive

defenses

that

address

vulnerabilities

at

every

stage

of

the

AI

lifecycle,

from

development

to

deployment.

We

identify

four

complementary

strategies

for

preserving

AI

integrity:
42

1.

AI

infrastructure

security
:

protects

the

systems,

networks,

and

processes

used

to

develop

and

deploy

frontier

AI

systems,

preventing

integrity

attacks

before

they

occur
.

This

approach

focuses

on

3

areas:

preserving

model

weight

integrity,

preserving

training

data

integrity,

and

securing

data

ﬁltering

algorithms.

2.

Data

auditing
:

addresses

the

trustworthiness

of

the

data

by

ensuring

the

data’s

quality,

integrity,

and

provenance.

This

approach

includes

developing

data

ﬁltering

algorithms

to

detect

and

remove

poisoned

content

as

well

as

maintaining

auditable

records

of

what

data

was

used

and

where

it

came

from.

3.

Model

auditing

and

evaluation
:

identiﬁes

whether

an

AI

system

has

been

compromised

after

training

is

complete

by

evaluating

the

model

itself.

This

approach

includes

behavioral

evaluations

that

probe

for

suspicious

patterns

(black-box

methods)

and

analysis

of

model

weights

to

locate

hidden

functionality

(white-box

methods).

4.

AI

control
:

acknowledges

that

we

may

never

achieve

complete

certainty

that

an

AI

system

remains

uncompromised.

AI

control

methods

focus

on

detecting

and

blocking

malicious

behavior

during

deployment

to

enable

the

safe

and

productive

use

of

a

potentially

untrusted

model.

This

approach

applies

zero

trust

principles

to

AI

systems:

just

as

zero

trust

network

architectures

assume

no

implicit

trust

based

on

location

or

ownership

and

continuously

authenticate

users

and

devices,

AI

control

assumes

no

implicit

trust

in

model

outputs

and

continuously

monitors

and

validates

AI

behavior.
43

AI

control

methods

include

real-time

monitoring,

restricted

autonomy,

and

isolation.

43

U.S.

Army

Cyber

Command,

“Zero

Trust.”

42

Note

that

our

four

strategies

for

preserving

AI

integrity

are

not

exhaustive.

For

example,

one

fruitful

approach

for

reducing

risk

from

compromised

AIs

is

to

procure

AIs

from

multiple

developers.

This

ensures

that

even

if

one

AI

developer

is

compromised

the

other

AI

developer’s

models

are

trustworthy.

In

practice,

this

could

look

like

the

government

jointly

procuring

AI

systems

from

OpenAI,

Anthropic,

and

Google

DeepMind.

Then,

government

employees

could

use

diﬀerent

AIs

to

check

each

other’s

work.

AI

INTEGRITY

|

20

Figure

4.

Summary

of

the

four

primary

approaches

to

preserving

AI

integrity.

Approach

1:

AI

Infrastructure

Security

This

ﬁrst

approach

aims

to

prevent

unauthorized

access

and

modiﬁcations

throughout

the

AI

development

and

deployment

lifecycle.

AI

infrastructure

has

a

massive

attack

surface,

so

we

focus

on

the

components

most

important

for

preserving

AI

integrity:

model

weight

integrity
,

training

data

integrity
,

and

security

of

data

ﬁltering

algorithms
.

Model

weight

integrity

ensures

that

AI

model

weights

remain

free

from

unauthorized

or

secret

modiﬁcations

during

both

training

and

inference.

In

practice,

this

means

preventing

attackers

from

“swapping”

legitimate

model

weights

with

poisoned

versions.
44

Preserving

model

weight

integrity

requires

addressing:

●

Inference

integrity

veriﬁcation
:

Periodically

verifying

that

served

models

match

reference

model

hashes.

Ideally,

this

integrity

veriﬁcation

could

happen

through

a

hardware-enforced

channel.

Verifying

integrity

during

training

is

signiﬁcantly

harder,

because

frequent

weight

updates

mean

there

is

no

stable

reference

hash

to

check

against.

One

promising

direction

44

Similarly,

we

may

also

be

concerned

about

system

prompt

swap

attacks.

A

malicious

system

prompt

could

include

the

password

trigger

for

a

backdoor,

for

example.

AI

INTEGRITY

|

21

is

developing

methods

for

deterministic,

replicable

training

runs

that

can

be

independently

audited.
45

Further

research

is

needed

on

integrity

veriﬁcation

during

training.

●

Model

provenance
:

Maintaining

comprehensive

audit

trails

requires

storing

snapshots

at

each

training

step.
46

Ensuring

model

provenance

may

involve

storing

a

data

structure

containing

some

or

all

of

the

following

information

at

each

gradient

step:

pre/post-update

weights,

gradients,

optimizer

states,

hyperparameters,

loss

values,

random

seeds,

and

training

data

batches.

Unfortunately,

this

would

likely

create

major

storage

bottlenecks.

Further

research

is

required

to

develop

a

scalable

solution

for

maintaining

model

provenance.

●

Deployment

controls
:

Deploying

new

models

should

require

strong

organizational

controls.

Multi-party

authorization

should

be

required

before

production

deployment,

with

independent

veriﬁcation

that

the

deployed

model

matches

authorized

checkpoints.

Logs

should

document

who

approved

deployment,

what

testing

occurred,

and

what

the

intended

model

behavior

should

be.

Training

data

integrity

ensures

that

training

data

remains

free

from

unauthorized

or

secret

modiﬁcations,

as

well

as

ensuring

that

the

data

is

high-quality

and

free

from

poisoning.

Preserving

training

data

integrity

requires

addressing:

●

Tamper-resistant

storage
:

Implementing

robust

access

controls

limiting

who

can

modify

datasets,

immutable

storage

systems
47

(e.g.,

write-once-read-many

[WORM]

drives,
48

blockchain-based

storage
49
),

multi-party

authorization

for

dataset

modiﬁcations,

and

periodic

integrity

checks

via

re-hashing.

●

Data

redundancy
:

Maintaining

multiple

copies

of

data

across

geographically

separated

locations

to

protect

against

accidental

corruption

and

targeted

attacks.

These

redundant

data

copies

should

ideally

be

tamper-proof

and

periodically

integrity

checked

via

hashing.

●

Transformation

logging
:

Recording

all

modiﬁcations,

ﬁlters,

and

transformations

applied

to

data.

This

creates

an

auditable

record

enabling

post-incident

investigation

if

compromised

data

is

later

discovered

and

helps

identify

which

transformations

may

have

introduced

poison.

49

Aniello

et

al.,

"A

Prototype

Evaluation

of

a

Tamper-Resistant

High

Performance

Blockchain-Based

Transaction

Log

for

a

Distributed

Database.";

Putz

et

al.,

"A

Secure

and

Auditable

Logging

Infrastructure

Based

on

a

Permissioned

Blockchain."

48

Guardiola

et

al.,

"The

Reverse

File

System:

Towards

Open

Cost-Eﬀective

Secure

WORM

Storage

Devices

for

Logging."

47

Ahmad

et

al.,

"HardLog:

Practical

Tamper-Proof

System

Auditing

Using

a

Novel

Audit

Device."

46

Training

an

AI

model

is

a

non-deterministic

process,

which

makes

model

provenance

auditing

diﬃcult.

If

auditors

are

unable

to

reproduce

a

training

run,

they

may

struggle

to

rule

out

foul

play.

Deterministic

training

warrants

further

research.

45

Shavit,

"What

Does

It

Take

to

Catch

a

Chinchilla?"

AI

INTEGRITY

|

22

●

Provenance

metadata
:

For

pre-training

data,

recording

stable

source

URLs

and

timestamps.

For

synthetic

data,

recording

which

model

generated

each

sample

(this

is

critical

for

preventing

subliminal

learning

attacks
50

since

such

attacks

work

best

when

the

model

is

trained

on

its

own

outputs
51
).

●

Third-party

data

veriﬁcation
:

Treating

externally-sourced

data

(e.g.,

from

Scale

AI
52
)

with

heightened

scrutiny.

Further

research

is

needed

on

methods

for

data

providers

to

credibly

assure

procurers

of

data

integrity,

such

as

auditable

chain-of-custody

records

or

cryptographic

provenance

guarantees.

Security

of

data

ﬁltering

algorithms

ensures

that

attackers

are

unable

to

compromise

the

conﬁdentiality

and

integrity

of

data

ﬁltering

algorithms.

Preserving

the

conﬁdentiality

of

data

ﬁltering

algorithms

makes

it

harder

for

attackers

to

iterate

on

the

defender’s

defenses

(i.e.,

if

the

attacker

does

not

understand

how

the

data

ﬁltering

algorithms

work,

then

they

will

have

a

harder

time

crafting

poisoned

data

that

bypasses

those

data

ﬁltering

algorithms).

Preserving

the

integrity

of

data

ﬁltering

algorithms

makes

it

diﬃcult

for

attackers

to

sabotage

the

data

ﬁltering

algorithms

through

“
algorithm

swap

attacks
,”

where

the

attacker

replaces

a

legitimate

data

ﬁltering

algorithm

with

a

more

inaccurate

one,

or

“algorithm

degradation

attacks,”

where

the

attacker

directly

tampers

with

the

development

of

data

ﬁltering

algorithms

to

make

them

inaccurate

or

unreliable.
53

Securing

data

ﬁltering

algorithms

requires

addressing:

●

Information

compartmentalization
:

Separating

teams

working

on

diﬀerent

ﬁltering

stages

(e.g.,

one

team

detects

spam,

another

handles

steganography)

to

prevent

insider

threats

from

understanding

the

complete

pipeline.
54

●

Algorithm

integrity

controls
:

Preventing

algorithm

swap

or

degradation

attacks

through

multi-party

authorization

for

updates

and

tamper-proof

audit

logs

documenting

all

changes.

Overall,

the

ﬁeld

of

securing

algorithmic

secrets

remains

signiﬁcantly

underdeveloped

and

requires

further

research.

54

Information

compartmentalization

has

downsides.

It

reduces

productivity,

which

could

result

in

lower-quality

data

ﬁlters.

It

also

concentrates

power

among

the

few

researchers

with

knowledge

of

the

ﬁltering

pipeline.

53

This

could

be

considered

a

“meta

poisoning

attack.”

Rather

than

directly

poisoning

the

frontier

AI’s

training

data,

the

attacker

compromises

the

data

used

to

train

the

ﬁlters

themselves.

By

degrading

the

accuracy

of

these

ﬁlters,

the

attacker

creates

a

path

to

successfully

poison

the

frontier

model

downstream.

52

Scale

AI,

“Data

Engine:

Data

Annotation,

Collection,

&

Curation

Platform.”

51

Subliminal

learning

occurs

when

a

teacher

model

with

some

trait

T

generates

innocuous

data

D

unrelated

to

T.

When

a

student

model

is

trained

on

D,

it

also

acquires

trait

T.

However,

subliminal

learning

only

works

if

the

student

and

teacher

models

are

derived

from

the

same

base

model.

In

the

context

of

data

poisoning

defenses,

this

means

frontier

AI

developers

should

treat

data

generated

by

the

frontier

model

being

trained

with

special

scrutiny,

as

the

subliminal

learning

eﬀect

may

enable

covert

trait

propagation.

50

Cloud

et

al.,

“Subliminal

Learning:

Language

Models

Transmit

Behavioral

Traits

via

Hidden

Signals

in

Data.”

AI

INTEGRITY

|

23

●

Canary

testing
:

Intentionally

planting

known-malicious

samples

that

legitimate

data

ﬁlters

should

catch.

If

these

known-malicious

samples

bypass

the

ﬁlters,

then

the

data

ﬁlters

may

have

been

compromised.

Many

of

the

security

measures

listed

above

impose

signiﬁcant

productivity

taxes,

creating

friction

that

prevents

industry

adoption.

Research

into

making

these

implementations

low-friction

and

developer-friendly

is

necessary

for

practical

deployment.

Additionally,

due

to

the

threat

posed

by

insider

threats,

we

recommend

frontier

AI

developers

strengthen

insider

threat

programs.

Approach

2:

Data

Auditing

The

second

approach

addresses

the

quality

trustworthiness

of

training

data

itself.

Since

AI

systems

learn

their

behaviors

from

training

data

rather

than

explicit

programming,

ensuring

data

integrity

is

critical

to

preventing

compromised

AI

models.

Data

auditing

measures

include:

●

Data

ﬁltering

algorithms
:

Employing

data

ﬁlters

to

detect

and

eliminate

poisoned

data

from

training

datasets.

●

Steganography

detection
:

Identifying

malicious

content

hidden

within

seemingly

benign

training

data,

where

backdoor

triggers

or

biases

are

steganographically

encoded

to

evade

standard

ﬁltering

techniques.
55

●

Data

attribution
:

Frameworks

for

tracing

speciﬁc

model

behaviors

back

to

speciﬁc

training

data

samples.
56

Unfortunately,

data

auditing

remains

signiﬁcantly

underdeveloped.

Training

datasets

often

contain

trillions

of

tokens

sourced

from

diverse

origins,

meaning

even

extraordinarily

accurate

ﬁlters

will

still

56

Berdoz

et

al.,

"Data

Attribution

in

Large

Language

Models

via

Bidirectional

Gradient

Optimization."

55

Cloud

et

al.,

“Subliminal

Learning:

Language

Models

Transmit

Behavioral

Traits

via

Hidden

Signals

in

Data.”

AI

INTEGRITY

|

24

allow

substantial

amounts

of

poisoned

data

through—enough

to

compromise

model

behavior.
57

Moreover,

attackers

can

craft

poisoned

data

speciﬁcally

designed

to

evade

automated

ﬁltering

(e.g.,

using

subliminal

learning

techniques

where

malicious

patterns

are

encoded

in

ways

that

appear

innocuous

to

current

detection

algorithms
58
).

As

AI

companies

increasingly

rely

on

training

on

synthetic

data,
59

ensuring

the

integrity

of

these

synthetic

datasets

should

become

a

high

priority.
60

We

think

some

of

the

most

important

open

problems

in

training

data

auditing

are:

●

Detecting

obfuscated

poisoned

data
.

Techniques

like

Phantom

Transfer

produce

poisoned

datasets

that

evade

even

oracle-level

defenses

where

the

defender

knows

exactly

what

the

attack

is

targeting.
61

To

the

best

of

our

knowledge,

there

are

no

techniques

for

detecting

inductive

backdoors,

phantom

transfer

attacks,

or

subliminal

learning

attacks.

●

Targeted

poisoned

data

retrieval
.

If

defenders

know

the

speciﬁc

backdoored

behavior

they

are

looking

for

(e.g.,

insecure

code

generation

or

pro-adversary

sentiment),

can

they

reliably

locate

the

responsible

training

samples?

This

is

a

more

tractable

variant

of

the

general

data

ﬁltering

problem

because

the

space

of

catastrophically

bad

behaviors

may

be

small.

●

Scaling

data

ﬁlters

without

sacriﬁcing

precision
.

Many

data

ﬁltering

techniques

achieve

strong

detection

rates

in

controlled

settings

but

become

impractical

at

scale

because

they

ﬁlter

out

too

much

benign

data

(i.e.,

high

false

positive

rate).

It

would

be

valuable

to

develop

ﬁlters

that

maintain

both

high

true

positive

rates

and

low

false

positive

rates

across

trillion-token

datasets.

61

Draganov

et

al.,

"Phantom

Transfer:

Data-level

Defences

are

Insuﬃcient

Against

Data

Poisoning."

60

More

speciﬁcally,

we

must

ensure

the

base

model

generating

synthetic

data

is

not

itself

compromised.

This

expands

the

attack

surface

considerably:

compromised

models

could

propagate

secret

loyalties

to

their

successors

through

the

synthetic

training

data

they

produce.

59

xAI,

“Grok

4.”

58

Cloud

et

al.,

“Subliminal

Learning:

Language

Models

Transmit

Behavioral

Traits

via

Hidden

Signals

in

Data.”

57

Souly

et

al.,

“A

small

number

of

samples

can

poison

LLMs

of

any

size.”;

To

illustrate

why

data

ﬁlters

require

extraordinary

accuracy,

let’s

assume

a

data

ﬁltering

algorithm

achieves

a

99.9%

true

positive

rate

in

ﬁltering

out

poisoned

data.

Based

on

Anthropic's

recent

paper

on

data

poisoning,

250

documents

averaging

1150

tokens

each

(250*1150=287K

total

poisoned

tokens)

suﬃced

to

backdoor

a

model.

Consider

a

frontier

model

with

5T

trainable

parameters

(similar

to

public

estimates

of

GPT-4.5’s

size)

trained

under

Chinchilla-optimal

scaling

(20

tokens

per

parameter).

Such

a

model

uses

5T*20=100T

total

training

tokens.

With

a

99.9%

true

positive

rate

data

ﬁlter,

an

attacker

would

need

287M

poisoned

tokens

to

successfully

backdoor

the

model—merely

0.00029%

of

the

training

corpus.

Furthermore,

the

number

of

poisoned

samples

required

to

backdoor

a

model

is

sensitive

to

ﬁlter

accuracy.

At

99%

true

positive

rate,

attackers

only

need

29M

poisoned

tokens

(0.000029%

of

corpus).

To

complicate

matters

further,

the

above

analysis

assumes

that

the

false

positive

rate

is

zero.

However,

in

realistic

scenarios,

the

data

ﬁlters

would

be

“catching”

signiﬁcant

amounts

of

benign

data

(i.e.,

a

high

false

positive

rate).

The

upshot

is

that

even

pretty

good

data

ﬁlters

will

hurt

downstream

model

capabilities.

AI

INTEGRITY

|

25

Approach

3:

Model

Auditing

and

Evaluation

The

third

approach

addresses

auditing

the

AI

model

itself
62
—examining

its

parameters

and

behavior

to

identify

tampering,

backdoors,

or

unauthorized

modiﬁcations.

There

are

two

primary

methods,

distinguished

by

whether

evaluators

examine

the

model's

behavior

or

its

internal

workings:

1.

Black-box

evaluation

probes

how

the

model

responds

to

carefully

designed

inputs

(without

access

to

model

weights).

Researchers

test

the

model

with

various

prompts

and

scenarios

to

identify

suspicious

patterns—for

instance,

whether

the

model

exhibits

systematic

bias

toward

CCP

narratives

when

asked

about

sensitive

geopolitical

topics.

Unfortunately,

black-box

evaluations

are

inadequate

and

are

unlikely

to

uncover

basic

backdoors

or

sophisticated

secret

loyalties.
63

2.

White-box

evaluation

examines

the

model's

internal

workings

directly

(with

access

to

model

weights).

Researchers

analyze

the

model's

parameters

and

internal

representations

to

identify

anomalies

that

might

indicate

tampering.

One

key

technique

is

mechanistic

interpretability,

a

ﬁeld

focused

on

reverse-engineering

AI

models

to

provide

insight

into

how

and

why

an

AI

model

exhibits

particular

behaviors.

While

more

technically

demanding,

white-box

methods

can

often

detect

backdoors

that

black-box

testing

misses.
64

Model

auditing

should

occur

throughout

the

development

process,

not

just

after

ﬁnal

training.

Frontier

AI

developers

should

implement

automated

evaluation

suites

that

run

black-box

and

white-box

tests

at

every

model

checkpoint—after

pre-training,

during

post-training

phases,

and

at

intermediate

stages.

This

requires

robust

model

ﬁngerprinting

and

version

control:

maintaining

cryptographically

signed

records

of

model

checkpoints

and

their

associated

metadata

(training

data

sources,

hyperparameters,

evaluation

results)

to

verify

that

each

model

version

matches

its

intended

state

and

to

detect

unauthorized

modiﬁcations

between

checkpoints.

Both

black-box

and

white-box

evaluation

techniques

face

signiﬁcant

challenges.

Frontier

AI

models

contain

hundreds

of

billions

or

trillions

of

parameters,

making

comprehensive

audits

computationally

expensive.

Moreover,

adversaries

could

design

backdoors

speciﬁcally

to

evade

detection

methods.

This

creates

an

ongoing

adversarial

dynamic

between

attackers

and

defenders,

where

each

advance

in

detection

capabilities

may

be

countered

by

more

sophisticated

attack

techniques.

64

Ibid.

63

Casper

et

al.,

“Black-Box

Access

is

Insuﬃcient

for

Rigorous

AI

Audits.”;

MacDiarmid

et

al.,

“Simple

Probes

Can

Catch

Sleeper

Agents.”

62

Approach

3

(model

auditing

and

evaluation)

beneﬁts

from

access

to

the

training

data,

so

in

most

circumstances,

it

is

advantageous

to

combine

approaches

2

(data

auditing)

and

3

(model

auditing

and

evaluation).

AI

INTEGRITY

|

26

Ultimately,

pure

black-box

evaluation

methods

seem

insuﬃcient

for

national

security

needs,

as

they

are

unlikely

to

uncover

some

integrity

violations.
65

Defense

eﬀorts

should

prioritize

multi-layered

strategies,

such

as

combining

white-box

evaluation

techniques

with

training

data

audits.

Approach

4:

AI

Control

The

fourth

approach

acknowledges

that

we

may

never

achieve

complete

certainty

that

an

AI

system's

integrity

has

been

preserved.

This

raises

an

important

question:

can

we

still

safely

and

productively

deploy

potentially

compromised

models?

Fortunately,

AI

control

oﬀers

an

answer.

AI

control

is

a

research

ﬁeld

focused

on

detecting

and

blocking

malicious

behavior

during

deployment

to

enable

the

safe

deployment

of

a

potentially

compromised

model
.
66

Rather

than

requiring

absolute

certainty

about

a

model's

integrity,

these

techniques

enable

organizations

to

beneﬁt

from

AI

systems

while

constraining

their

potential

for

harm.

This

approach

is

reﬂected

in

the

White

House

AI

Action

Plan,

which

calls

for

investment

in

"AI

control

systems"

as

part

of

its

strategy

for

AI

security.
67

AI

control

extends

zero

trust

principles

from

network

security

to

AI

systems.

Traditional

network

defenses

assumed

everything

behind

a

ﬁrewall

was

safe;

zero

trust

instead

requires

continuous

veriﬁcation

of

every

user

and

device.
68

Similarly,

AI

control

rejects

the

assumption

that

a

model

passing

pre-deployment

evaluation

can

be

trusted

thereafter,

instead

requiring

ongoing

validation

of

AI

behavior

throughout

operation.

AI

control

techniques

include:

●

Real-time

monitoring
:

Logging

all

AI

system

interactions

and

outputs

for

human

review,

with

particular

scrutiny

for

sensitive

operations

●

Limited

autonomy
:

Restricting

AI

systems

to

narrow,

well-deﬁned

tasks

rather

than

granting

broad

decision-making

authority

●

Sandboxing
:

Deploying

AI

systems

in

isolated

environments

where

potential

damage

from

compromised

behavior

can

be

contained

●

Chain-of-thought

monitoring
:

Inspecting

a

model's

intermediate

reasoning

steps

to

detect

deceptive

or

misaligned

intent

before

ﬁnal

outputs

are

executed
69

An

added

beneﬁt

of

AI

control

is

that

if

malicious

behavior

is

detected

during

deployment,

the

compromised

models

can

be

decommissioned.

While

the

previous

three

approaches

to

preserving

integrity

provide

assurance

during

development
,

approach

four

(AI

control)

provides

assurance

69

Delaney

et

al.,

"Policy

Options

for

Preserving

Chain

of

Thought

Monitorability."

68

U.S.

Army

Cyber

Command,

“Zero

Trust.”

67

The

White

House,

“Winning

the

Race:

America’s

AI

Action

Plan.”

66

Greenblatt

et

al.,

“AI

Control:

Improving

Safety

Despite

Intentional

Subversion.”

65

Ibid.

AI

INTEGRITY

|

27

during

deployment
.

For

a

comprehensive

discussion

of

open

problems

in

AI

control

research,

see

Greenblatt.
70

A

Defense-in-Depth

Strategy

Currently,

all

four

approaches

remain

signiﬁcantly

underdeveloped.

AI

infrastructure

security

involves

challenging

engineering

problems,

and

current

solutions

potentially

impose

substantial

operational

costs

that

can

slow

AI

development

cycles.

Data

auditing

techniques

struggle

with

detecting

poisoned

content

hidden

through

steganographic

techniques.

Model

auditing

methods

struggle

to

identify

backdoors

embedded

within

trillions

of

parameters.

AI

control

remains

the

least

developed

approach,

with

signiﬁcant

open

questions

about

implementation

and

eﬀectiveness.

A

defense-in-depth

strategy

requires

investment

across

all

four

approaches

simultaneously.

No

single

method

provides

complete

protection;

only

by

layering

these

complementary

defenses

can

we

build

integrity-preserving

AI

systems.

70

Greenblatt,

"An

Overview

of

Areas

of

Control

Work."

AI

INTEGRITY

|

28

4

|

Policy

Recommendations

for

AI

Integrity

Preserving

AI

integrity

cannot

be

solved

by

industry

alone.

Frontier

AI

companies

face

a

threat

landscape

that

demands

capabilities

beyond

typical

corporate

security.

More

speciﬁcally,

defending

against

nation-state

intelligence

services

and

insider

threats

requires

specialized

expertise

that

most

companies

lack.

Moreover,

the

technical

problems

of

detecting

backdoors

in

trillion-parameter

models

and

preventing

tampering

across

complex

development

pipelines

remain

largely

unsolved.

While

AI

companies

employ

talented

security

teams,

they

are

constrained

by

limited

resources,

competing

priorities,

and

the

need

to

maintain

rapid

development

cycles

in

a

competitive

market.

The

US

government

is

uniquely

positioned

to

address

these

gaps

through

strategic

investment

and

coordination.

Federal

agencies

possess

decades

of

experience

countering

nation-state

adversaries

and

insider

threats.

Research

organizations

like

Intelligence

Advanced

Research

Projects

Activity

(IARPA)

and

the

National

Institute

of

Standards

and

Technology

(NIST)

have

proven

track

records

of

mobilizing

cutting-edge

technical

solutions

to

national

security

challenges.

And

government

procurement

power

can

create

strong

incentives

for

industry

adoption

of

security

best

practices

without

imposing

heavy-handed

regulation

that

could

stiﬂe

innovation.

We

recommend

four

complementary

actions

to

strengthen

AI

integrity:

1.

Organize

government-led

red

team

exercises

where

teams

from

the

Intelligence

Community

(IC)

test

infrastructure

security,

and

private

machine

learning

(ML)

security

companies

attempt

to

poison

frontier

AI

models.

2.

Create

voluntary

NIST

security

frameworks

providing

concrete

technical

guidance

for

protecting

AI

systems

throughout

their

development

lifecycle.

3.

Establish

an

AI

Information

Sharing

and

Analysis

Center

(AI-ISAC)

enabling

mutual

threat

intelligence

sharing

between

frontier

AI

developers

and

national

security

agencies.

4.

Launch

new

ARPA

programs

hiring

three

program

managers

focused

on

model

subversion

detection,

AI

infrastructure

security,

and

AI

control

systems.

AI

INTEGRITY

|

29

Table

3.

Summary

of

AI

integrity

policy

recommendations.

Recommendation

1:

Organize

Government-Led

Red

Team

Exercises

The

US

government

should

fund

periodic

red

team

exercises

where

expert

teams

attempt

to

compromise

the

integrity

of

AI

systems

at

frontier

companies
.

This

recommendation

for

government-led

red

teaming

has

clear

historical

precedent.

In

1997,

the

DOD

conducted

Eligible

Receiver

97

(ER97),

a

classiﬁed

exercise

in

which

an

NSA

Red

Team

used

only

publicly

available

tools

and

oﬀ-the-shelf

equipment

to

simulate

coordinated

attacks

against

US

critical

infrastructure

and

military

networks.
71

The

exercise

revealed

that

existing

defenses

were

inadequate

even

against

relatively

unsophisticated

attacks,

exposing

vulnerabilities

across

government

and

critical

infrastructure.

These

ﬁndings

directly

catalyzed

the

formation

of

what

would

eventually

become

US

Cyber

Command.

The

proposed

AI

integrity

red

team

program

seeks

to

replicate

this

model,

using

government-led

adversarial

exercises

to

reveal

vulnerabilities

in

AI

systems

before

real

adversaries

exploit

them

and

to

generate

institutional

momentum

for

defensive

reforms.

71

Martelle,

"Eligible

Receiver

97."

AI

INTEGRITY

|

30

A

successful

AI

integrity

attack

typically

requires

completing

a

kill

chain

with

two

distinct

phases:

(1)

compromising

the

infrastructure

through

network

intrusion,

credential

theft,

or

insider

access,

followed

by

(2)

exploiting

the

machine

learning

(ML)

development

process

through

model

sabotage

or

model

subversion.
72

Traditional

cybersecurity

red

teams

excel

at

infrastructure

compromise

but

typically

lack

expertise

in

ML

attacks,

while

ML

security

specialists

understand

model-level

vulnerabilities

but

may

not

possess

nation-state-level

operational

tradecraft.

Rather

than

attempting

to

source

rare

teams

with

deep

expertise

in

both

domains,

this

program

decouples

the

exercises,

allowing

specialized

teams

to

focus

on

their

areas

of

strength

while

still

testing

the

complete

attack

surface.

To

operationalize

this

program,

the

Department

of

Homeland

Security

(DHS),

DOD,

or

IC

should

establish

a

red

team

program

with

two

complementary

components:

1.

Infrastructure

compromise

exercises

led

by

IC

teams

focused

on

gaining

unauthorized

access

to

training

data

repositories,

compute

clusters,

and

development

pipelines.

2.

ML-speciﬁc

attack

exercises

conducted

by

specialized

security

ﬁrms

(e.g.,

Gray

Swan

AI,

Palisade

Research,

Trail

of

Bits)

that

assume

various

levels

of

access
73

and

attempt

model

subversion

or

sabotage

attacks.
74

The

results

of

the

exercises

should

be

classiﬁed

to

prevent

creating

roadmaps

for

adversaries,

though

anonymized

lessons

should

be

shared

across

participating

companies

to

raise

the

defensive

baseline

industry-wide.

The

program

should

begin

with

a

pilot

phase

targeting

1–2

major

AI

companies

as

voluntary

participants

to

demonstrate

value

and

reﬁne

methodology.

This

initial

phase

would

establish

74

ML

attack

exercises

should

target

dedicated

test

infrastructure

(isolated

compute

clusters,

replica

training

pipelines,

representative

checkpoints)

rather

than

production

systems.

Attacking

an

actual

training

run

risks

irreversible

model

corruption

and

could

cost

millions

in

wasted

compute

(we

acknowledge

this

approach

trades

some

realism

for

safety,

and

we

are

not

conﬁdent

whether

targeting

test

infrastructure

is

suﬃciently

realistic).

These

ML

attack

exercises

should

follow

a

progressive

diﬃculty

structure:

initial

rounds

grant

red

teams

maximal

aﬀordances

(full

system

access,

knowledge

of

defenses,

extended

timelines),

then

systematically

reduce

advantages

in

subsequent

rounds.

This

reveals

the

minimum

defensive

posture

required

for

blue

teams

to

successfully

detect

and

block

attacks,

informing

practical

security

requirements

for

frontier

AI

development.

73

Davidson,

“ML

Research

Directions

for

Preventing

Catastrophic

Data

Poisoning.”

72

Note

that

compromising

the

infrastructure

is

not

necessary

for

integrity

attacks

that

only

involve

poisoning

public

pre-training

datasets.

Regarding

pre-training

data

poisoning

attacks,

we

are

uncertain

how

to

red

team

such

attacks.

Pre-training

attacks

need

to

“survive”

throughout

the

entire

development

lifecycle—that

is,

poisoning

a

model

in

the

pre-training

phase

might

not

work

because

the

post-training

phase

may

result

in

the

poisoned

behavior

being

“trained

away.”

If

the

pre-training

attack

is

successful

and

it

is

diﬃcult

to

unlearn

the

poisoned

behavior,

then

the

frontier

developer

may

have

to

restart

their

training

run,

which

would

be

ﬁnancially

catastrophic.

AI

INTEGRITY

|

31

baseline

procedures,

identify

operational

challenges,

and

build

trust

with

frontier

AI

developers

before

scaling.

Following

a

successful

pilot

completion,

the

program

should

expand

through

a

phased

approach.

Year

two

could

add

2–3

additional

voluntary

participants,

incorporating

lessons

learned

from

the

pilot

phase.

By

year

three,

participation

could

become

mandatory

for

all

frontier

AI

developers

holding

federal

contracts

exceeding

some

dollar-value

threshold

or

those

designated

as

critical

infrastructure.

This

timeline

provides

suﬃcient

runway

for

companies

to

strengthen

their

security

posture

while

ensuring

comprehensive

coverage

across

the

frontier

AI

ecosystem

within

a

reasonable

timeframe.

Recommendation

2:

Create

Voluntary

AI

Security

Frameworks

NIST,

in

collaboration

with

the

Center

for

AI

Standards

and

Innovation

(CAISI),

should

develop

voluntary

security

standards

speciﬁcally

designed

for

frontier

AI

developers.

These

standards

should

provide

concrete

technical

and

organizational

guidance

focused

on

two

security

pillars:

conﬁdentiality

(protecting

model

weights,

training

data,

and

algorithmic

innovations)

and

integrity

(ensuring

AI

systems

remain

free

from

unauthorized

modiﬁcations

or

secret

loyalties).

By

establishing

clear

standards

rather

than

mandatory

auditing

requirements,

this

approach

allows

companies

to

adopt

protections

appropriate

to

their

risk

proﬁle

while

creating

benchmarks

for

government

procurement.

Several

recent

initiatives

point

toward

comprehensive

AI

security

frameworks,

such

as

The

White

House

AI

Action

Plan’s

call

for

securing

AI

infrastructure

and

promoting

secure-by-design

AI

technologies,

and

the

SL5

Task

Force’s

development

of

standards

for

protecting

AI

model

weights

against

top

nation-state

threat

actors.
75

Building

on

these

eﬀorts,

we

propose

that

integrity

protections

be

integrated

into

these

standards

rather

than

treated

as

a

separate

standard.

A

comprehensive

approach

addressing

conﬁdentiality

and

integrity

together

provides

clearer

guidance

for

industry

and

avoids

fragmenting

security

requirements

across

multiple

competing

frameworks.

Following

the

RAND

security

level

(SL)

framework,
76

these

standards

should

deﬁne

three

progressive

security

levels

calibrated

to

threat

actor

capability:

●

Level

1

(SL3

Integrity

Protections)
:

Defends

against

cybercrime

syndicates

and

insider

threats,

including

world-renowned

criminal

hacker

groups,

well-resourced

terrorist

76

Nevo

et

al.,

“Securing

AI

Model

Weights:

Preventing

Theft

and

Misuse

of

Frontier

Models.”

75

The

White

House,

“Winning

the

Race:

America’s

AI

Action

Plan.”;

SL5

Task

Force,

“SL5

Task

Force

-

Security

Level

5

for

Frontier

AI.”;

Grunewald

and

Gershovich,

“Accelerating

AI

Data

Center

Security.”

AI

INTEGRITY

|

32

organizations,

and

disgruntled

employees.

These

actors

operate

with

budgets

up

to

$1

million

and

teams

of

roughly

10

experienced

professionals.

●

Level

2

(SL4

Integrity

Protections)
:

Defends

against

standard

operations

by

leading

cyber-capable

institutions,

including

many

foreign

intelligence

agencies

and

state-sponsored

groups.

These

operations

deploy

approximately

100

individuals

with

diverse

expertise

(e.g.,

cybersecurity,

human

intelligence,

physical

operations)

over

roughly

one

year

with

budgets

up

to

$10

million.

●

Level

3

(SL5

Integrity

Protections)
:

Defends

against

top-priority

operations

by

the

most

capable

nation-states.

These

operations

can

deploy

1,000

individuals

over

multiple

years

with

budgets

approaching

$1

billion.

The

standard

should

be

developed

in

three

phases.

First,

Level

1

protections

should

be

established

to

protect

against

operational

capacity

3

(OC3)

threats.

Second,

the

standard

should

be

extended

to

Level

2

protections

against

operational

capacity

4

(OC4)

threats.

Finally,

Level

3

protections

against

operational

capacity

5

(OC5)

threats

should

be

developed

once

the

necessary

technologies

mature.

This

phased

approach

allows

iterative

reﬁnement

while

acknowledging

that

defenses

against

OC4

and

OC5

threat

actors

require

additional

R&D

before

becoming

production-ready.

The

standards

should

be

scoped

to

include

AI

development

and

deployment

security
.

In

development

security,

the

standard

should

address

data

provenance

tracking,

model

versioning

and

ﬁngerprinting,

access

controls

and

multi-party

authorization,

and

insider

threat

monitoring.

In

deployment

security,

the

standard

should

address

model

and

system

prompt

attestation,
77

model

spec

attestation,
78

and

model

weight

integrity

veriﬁcation.
79

By

establishing

these

standards

through

NIST,

the

government

provides

clear

security

guidance

without

imposing

rigid

mandates.

Companies

also

gain

a

roadmap

for

building

trustworthy

systems,

and

government

agencies

gain

assurance

that

procured

AI

systems

meet

appropriate

security

thresholds.

In

the

end,

the

broader

AI

ecosystem

beneﬁts

from

shared

security

baselines

that

raise

the

defensive

ﬂoor

across

the

industry.

Recommendation

3:

Establish

an

AI

Information

Sharing

and

Analysis

Center

The

DHS

should

establish

an

AI

Information

Sharing

and

Analysis

Center

(AI-ISAC)

that

enables

threat

intelligence

sharing

between

frontier

AI

developers,

data

center

operators,

79

I.e.,

verifying

that

deployed

model

weights

match

the

cryptographically

signed

hash

of

the

authorized

reference

weights

through

periodic

integrity

checks.

78

OpenAI,

“OpenAI

Model

Spec.”;

Anthropic,

“Claude’s

Constitution.”

I.e.,

proving

to

the

user

that

a

given

model

was

trained

via

a

speciﬁc

model

spec

or

constitution.

77

I.e.,

proving

to

the

user

that

they

are

interacting

with

the

claimed

model

version

and

system

prompt.

AI

INTEGRITY

|

33

and

national

security

agencies.

This

partnership

would

enable

mutual

intelligence

ﬂows:

government

agencies

would

share

threat

actor

proﬁles

and

attribution

analysis

linking

attack

patterns

to

speciﬁc

adversaries,

zero-day

vulnerability

intelligence

aﬀecting

AI

development

infrastructure,

and

real-time

alerts

about

ongoing

operations

targeting

the

AI

sector,

while

companies

would

share

incident

reports,

technical

details

of

newly

discovered

attack

vectors,

and

early

warning

indicators

of

coordinated

campaigns.

By

coordinating

threat

intelligence

across

frontier

AI

developers,

each

company

gains

visibility

into

attack

patterns

and

vulnerabilities

that

others

have

observed,

strengthening

collective

defenses.
80

The

AI

Action

Plan

includes

a

related

recommendation,

calling

for

establishment

of

an

“AI

Information

Sharing

and

Analysis

Center

(AI-ISAC),

led

by

DHS,

in

collaboration

with

CAISI

at

DOC

[Department

of

Commerce]

and

the

Oﬃce

of

the

National

Cyber

Director,

to

promote

the

sharing

of

AI-security

threat

information

and

intelligence

across

US

critical

infrastructure

sectors.”
81

However,

the

AI

Action

Plan’s

proposed

AI-ISAC

only

focuses

on

critical

infrastructure

sectors

that

use

AI

systems

rather

than

the

companies

that

develop

frontier

AI.

Protecting

the

integrity

of

frontier

AI

development

requires

extending

intelligence

sharing

to

include

both

developers

and

infrastructure

operators.

The

AI-ISAC

should

address

not

only

traditional

cybersecurity

threats

but

also

ML-speciﬁc

attacks.

Traditional

ISACs

focus

on

information

sharing

of

the

cybersecurity

threat

landscape,

but

frontier

AI

developers

face

a

diﬀerent

threat

landscape.
82

Sharing

information

about

attacks

like

data

poisoning

is

not

necessarily

protected

under

existing

antitrust

safe

harbors.

Thus,

the

DHS

must

explicitly

establish

a

safe

harbor

for

frontier

AI

developers

to

share

ML-speciﬁc

attacks,

and

not

classify

these

attacks

as

“competitively

sensitive

business

information.”

Industry

initiatives

like

the

Frontier

Model

Forum's

information

sharing

agreement
83

demonstrate

that

AI

companies

recognize

the

need

for

coordination,

but

these

eﬀorts

lack

government

participation

and

the

legal

protections

necessary

for

sharing

sensitive

competitive

information.

The

AI-ISAC

should

consist

of

the

frontier

AI

developers

(OpenAI,

Anthropic,

Google

DeepMind,

Meta,

xAI),

data

center

operators

(AWS,

Azure,

GCP,

Oracle

Cloud),

and

national

security

agencies

(NSA,

FBI,

CISA,

and

ODNI).

This

partnership

should

draw

lessons

from

successful

programs

like

the

Defense

Industrial

Base

Cybersecurity

program
84

and

Financial

Services

ISAC.
85

85

FS-ISAC,

“Financial

Services

Information

Sharing

and

Analysis

Center.”

84

U.S.

Department

of

Defense,

“Defense

Industrial

Base

Cybersecurity

Strategy

2024.”

83

Frontier

Model

Forum,

“FMF

Information-Sharing.”

82

The

White

House,

“FACT

SHEET:

Executive

Order

Promoting

Private

Sector

Cybersecurity

Information

Sharing.”

81

The

White

House,

“Winning

the

Race:

America’s

AI

Action

Plan.”

80

National

Council

of

ISACs,

“National

Council

of

ISACs.”

AI

INTEGRITY

|

34

Recommendation

4:

Launch

New

ARPA

Programs

for

AI

Integrity

Research

Preserving

AI

integrity

requires

solving

two

distinct

classes

of

technical

challenges:

(1)

cybersecurity

threats

and

(2)

machine

learning

threats.

While

defending

against

standard

actors

relies

on

known

engineering

best

practices,

protecting

against

top-tier

nation-state

operations

(OC5)

involves

genuinely

unsolved

research

problems.

For

example,

securing

distributed

training

clusters

against

such

threats

requires

fundamental

breakthroughs

in

trusted

system

architecture.

Similarly,

the

machine

learning

dimension

presents

genuinely

unsolved

research

problems.

Detecting

poisoned

data

in

trillion-token

training

datasets,

identifying

steganographically

encoded

data,

and

auditing

frontier-scale

models

for

hidden

objectives

all

require

research

breakthroughs.

These

problems

are

inherently

high-risk,

high-reward

research

challenges

suited

for

Advanced

Research

Projects

Agencies

(ARPAs).

We

recommend

that

ARPAs

(e.g.,

DARPA,

IARPA,

HSARPA,

ARIA)

source

three

new

program

managers

with

proven

track

records

in

ML

and

security,

each

focused

on

a

distinct

approach

to

AI

integrity.

Program

1:

Model

Subversion

Detection
.

This

program

focuses

on

developing

techniques

to

audit

training

data

and

AI

models

for

poisoning

and

secret

loyalties,

building

on

the

success

of

IARPA's

TrojAI

program.
86

This

program

should

be

structured

around

blue-team

versus

red-team

audits

to

mirror

real-world

adversarial

situations.
87

Research

areas

may

include:

●

Identifying

speciﬁc

circuits

or

mechanisms

in

model

weights

and

activations

that

exist

if

and

only

if

a

backdoor

has

been

planted
88

●

Investigating

how

innocuous-seeming

data

can

be

used

to

instill

secret

loyalties
89

●

Developing

"last-mover"

advantages

for

blue

teams,

such

as

techniques

to

"train

out"

or

override

unknown

backdoors.
90

Program

2:

AI

Infrastructure

Security.

This

program

would

focus

on

developing

security

architectures

to

protect

the

physical

and

digital

infrastructure

used

to

train

and

deploy

frontier

AI

models.

For

a

detailed

discussion

of

research

areas

in

AI

infrastructure

security,

see

the

"
Approach

1:

AI

Infrastructure

Security
"

section

of

this

report.

90

Davidson,

“ML

Research

Directions

for

Preventing

Catastrophic

Data

Poisoning.”

89

Betley

et

al.,

“Weird

Generalization

and

Inductive

Backdoors:

New

Ways

to

Corrupt

LLMs.”;

Cloud

et

al.,

“Subliminal

Learning:

Language

Models

Transmit

Behavioral

Traits

via

Hidden

Signals

in

Data.”

88

MacDiarmid

et

al.,

“Simple

Probes

Can

Catch

Sleeper

Agents.”;

Yu

et

al.,

“Backdoor

Attribution:

Elucidating

and

Controlling

Backdoors

in

Language

Models.”

87

Davidson,

“ML

Research

Directions

for

Preventing

Catastrophic

Data

Poisoning.”;

Draganov

et

al.,

"Phantom

Transfer:

Data-level

Defences

are

Insuﬃcient

Against

Data

Poisoning."

86

Intelligence

Advanced

Research

Projects

Activity,

"TrojAI:

Trojans

in

Artiﬁcial

Intelligence."

AI

INTEGRITY

|

35

Program

3:

AI

Control

Systems
.

This

program

would

focus

on

building

technologies

that

enable

getting

useful

work

out

of

untrusted

AI

models:

real-time

monitoring

systems

that

detect

malicious

behavior

during

deployment;

least-privilege

frameworks

that

limit

AI

access

to

only

essential

information;
91

and

multi-model

veriﬁcation

protocols

where

independent

systems

must

agree

before

high-stakes

actions.
92

For

a

detailed

discussion

of

open

research

problems

in

AI

control,

see

Greenblatt.
93

We

also

recommend

establishing

a

Bay

Area

oﬃce

to

enable

recruitment

of

top

ML

and

security

talent

who

cannot

relocate

to

the

East

Coast.

Oﬀering

part-time

program

manager

positions

could

also

signiﬁcantly

expand

the

talent

pool,

as

many

top

researchers

cannot

fully

leave

their

primary

positions

but

could

contribute

1–2

days

per

week

to

high-impact

government

research

programs.

To

maximize

the

impact

of

these

ARPA

programs,

we

suggest

the

programs

directly

partner

with

frontier

AI

developers.

These

partnerships

could

involve:

●

Secondment

programs

where

company

researchers

spend

6–12

months

working

on

ARPA

projects

while

maintaining

industry

aﬃliations

●

Joint

research

agreements

that

allow

frontier

companies

to

contribute

proprietary

datasets

and

model

access

for

security

research

●

Regular

technical

working

groups

that

bring

together

government,

industry,

and

academic

researchers

to

share

ﬁndings

(with

appropriate

classiﬁcation

controls)

93

Greenblatt,

"An

Overview

of

Areas

of

Control

Work."

92

Kalai

et

al.,

"Consensus

Sampling

for

Safer

Generative

AI.";

Ron

et

al,

"Galápagos:

Automated

N-Version

Programming

with

LLMs.";

Wei

et

al.

"CORTEX:

Collaborative

LLM

Agents

for

High-Stakes

Alert

Triage."

91

Debenedetti

et

al.,

“Defeating

Prompt

Injections

by

Design.”

AI

INTEGRITY

|

36

5

|

Conclusion

The

rapid

integration

of

AI

systems

across

government

operations

increases

exposure

to

AI

integrity

threats.

As

adversaries

develop

both

the

capability

and

motivation

to

compromise

frontier

AI

systems,

establishing

robust

defenses

becomes

increasingly

important.

The

four

recommendations

outlined

in

this

report

provide

a

strategy

that

leverages

the

government's

unique

strengths

without

imposing

regulatory

burdens

on

industry.

By

organizing

government-led

red

team

exercises,

developing

voluntary

NIST

security

frameworks,

creating

formal

threat

intelligence

sharing

partnerships,

and

launching

new

ARPA

research

programs,

the

government

can

signiﬁcantly

strengthen

AI

integrity

across

both

public

and

private

sectors.

The

path

forward

requires

partnership

between

government

and

industry,

combining

the

government's

counterintelligence

expertise

with

industry's

technical

innovation.

By

implementing

these

recommendations,

the

United

States

can

maintain

its

leadership

in

AI

while

ensuring

that

the

systems

underpinning

critical

national

functions

remain

trustworthy

and

aligned

with

American

interests.

Many

open

questions

remain

about

how

best

to

tackle

the

problem

of

AI

integrity,

and

we

therefore

encourage

the

research

community

to

contribute

to

this

nascent

ﬁeld
.

AI

INTEGRITY

|

37

Acknowledgements

We

are

grateful

to

the

following

people

for

providing

valuable

feedback

and

insights:

Abbey

Chaver,

Stefan

Torges,

Evan

Miyazono,

Tom

Davidson,

Houlton

McGuinn,

Erich

Grunewald,

Matt

Hodak,

Nitzan

Shulman,

and

Matthew

Margo.

Special

thanks

to

Ashwin

Acharya

for

encouraging

us

to

begin

research

in

this

area.

Acknowledgment

does

not

imply

endorsement

of

all

claims

or

conclusions

in

this

report.

AI

INTEGRITY

|

38

Bibliography

Ahmad,

Adil,

Sangho

Lee,

and

Marcus

Peinado.

"HardLog:

Practical

Tamper-Proof

System

Auditing

Using

a

Novel

Audit

Device."

Microsoft

Research,

2022.

https://www.microsoft.com/en-us/research/wp-content/uploads/2022/04/hardlog-sp22.pdf.

Amodei,

Dario.

“The

Urgency

of

Interpretability.”

April

2025.

https://www.darioamodei.com/post/the-urgency-of-interpretability.

Aniello,

Leonardo,

Roberto

Baldoni,

Edoardo

Gaetani,

et

al.

"A

Prototype

Evaluation

of

a

Tamper-Resistant

High

Performance

Blockchain-Based

Transaction

Log

for

a

Distributed

Database."

IEEE,

2017.

https://ieeexplore.ieee.org/abstract/document/8123568?casa_token=491eRYXZm0cAAAAA:PyQg0
zUk_MBki1tpMFfWO2yuI8-H1Fw91U7oA2Bx1HVZ2hitaO_RAgmhziNgD6yebwvGBM5lmjLu

Anthropic.

“Claude’s

Constitution.”

May

9,

2023.

https://www.anthropic.com/news/claudes-constitution.

Anthropic.

“Measuring

political

bias

in

Claude.”

November

13,

2025.

https://www.anthropic.com/news/political-even-handedness

Anthropic.

“What

Is

Interpretability?”

Youtube,

2024.

https://www.youtube.com/watch?v=TxhhMTOTMDg&t=42s.

Berdoz,

Frédéric,

Luca

A.

Lanzendörfer,

Kaan

Bayraktar,

and

Roger

Wattenhofer.

"Data

Attribution

in

Large

Language

Models

via

Bidirectional

Gradient

Optimization."

Third

International

AI

Governance

Workshop,

January

2026.

https://openreview.net/forum?id=b8LB75iwNH.

Under

review.

Betley,

Jan,

Jorio

Cocola,

Dylan

Feng,

et

al.

"Weird

Generalization

and

Inductive

Backdoors:

New

Ways

to

Corrupt

LLMs."

arXiv,

December

10,

2025.

https://doi.org/10.48550/arXiv.2512.09742.

Bostrom,

Nick.

Superintelligence:

Paths,

Dangers,

Strategies,

2014.

Bowen,

Dillon,

Brendan

Murphy,

Will

Cai,

David

Khachaturov,

Adam

Gleave,

and

Kellin

Pelrine.

“Scaling

Laws

for

Data

Poisoning

in

LLMs.”

arXiv,

October

17,

2024.

https://arxiv.org/html/2408.02946v3.

Carlsmith,

Joe.

“Scheming

AIs:

Will

AIs

Fake

Alignment

during

Training

in

Order

to

Get

Power?”

arXiv,

November

27,

2023.

https://arxiv.org/abs/2311.08379.

Carreyrou,

John.

Bad

Blood:

Secrets

and

Lies

in

a

Silicon

Valley

Startup.

Knopf,

2018.

Casper,

Stephen,

Carson

Ezell,

Charlotte

Siegmann,

et

al.

“Black-Box

Access

Is

Insuﬃcient

for

Rigorous

AI

Audits.”

ACM

Digital

Library,

June

3,

2024.

https://dl.acm.org/doi/10.1145/3630106.3659037.

Center

for

AI

Standards

and

Innovation.

“Evaluation

of

DeepSeek

AI

Models.”

NIST,

September

30,

2025.

https://www.nist.gov/system/ﬁles/documents/2025/09/30/CAISI_Evaluation_of_DeepSeek_AI_Mode
ls.pdf.

Cherny,

Boris

(@bcherny).

"When

I

created

Claude

Code

as

a

side

project

back

in

September

2024,

I

had

no

idea

it

would

grow

to

be

what

it

is

today.

It

is

humbling

to

see

how

Claude

Code."

X,

December

27,

2025.

https://x.com/bcherny/status/2004887829252317325.

Cloud,

Alex,

Minh

Le,

James

Chua,

et

al.

“Subliminal

Learning:

Language

Models

Transmit

Behavioral

Traits

via

Hidden

Signals

in

Data.”

Alignment

Science

Blog,

July

22,

2025.

https://alignment.anthropic.com/2025/subliminal-learning/.

Davidson,

Tom.

“ML

Research

Directions

for

Preventing

Catastrophic

Data

Poisoning.”

Forethought,

January

7,

2026.

https://www.forethought.org/research/ml-research-directions-for-preventing-catastrophic-data-pois
oning.

AI

INTEGRITY

|

39

Debenedetti,

Edoardo,

Ilia

Shumailov,

Tianqi

Fan,

et

al.

“Defeating

Prompt

Injections

by

Design.”

arXiv,

March

24,

2025.

https://arxiv.org/abs/2503.18813.

Delaney,

Oscar,

Oliver

Guest,

and

Renan

Araujo.

"Policy

Options

for

Preserving

Chain

of

Thought

Monitorability."

Institute

for

AI

Policy

and

Strategy,

September

24,

2025.

https://www.iaps.ai/research/policy-options-for-preserving-cot-monitorability.

Draganov,

Andrew,

Tolga

H.

Dur,

Anandmayi

Bhongade,

and

Mary

Phuong.

"Phantom

Transfer:

Data-level

Defences

are

Insuﬃcient

Against

Data

Poisoning."

arXiv,

February

3,

2026.

https://arxiv.org/abs/2602.04899.

Eichenwald,

Kurt.

Conspiracy

of

Fools:

A

True

Story.

Broadway

Books,

2005.

Ernst

&

Young.

“EY

Pulse

Survey:

Insights

into

the

Integration

of

AI

in

Government.”

August

2024.

https://www.ey.com/content/dam/ey-uniﬁed-site/ey-com/en-us/industries/government-public-sector
/documents/ey-public-sector-ai-pulse-survey-us-score-no-24250-241us.pdf.

Figueroa,

Marco

and

Pliny

the

Liberator.

“Poison

in

the

Pipeline:

Liberating

Models

with

Basilisk

Venom.”

0DIN,

February

6,

2025.

https://0din.ai/blog/poison-in-the-pipeline-liberating-models-with-basilisk-venom.

Frontier

Model

Forum.

“FMF

Information-Sharing.”

2025.

https://www.frontiermodelforum.org/information-sharing/.

FS-ISAC.

“Financial

Services

Information

Sharing

and

Analysis

Center.”

Accessed

November

14,

2025.

https://www.fsisac.com/.

Fu,

Tingchen,

Mrinank

Sharma,

Philip

Torr,

Shay

B.

Cohen,

David

Krueger,

and

Fazl

Barez.

“PoisonBench:

Assessing

Large

Language

Model

Vulnerability

to

Data

Poisoning.”

arXiv,

June

6,

2024.

https://arxiv.org/abs/2410.08811.

Gilesarchive,

Martin.

“Triton

Is

the

World’s

Most

Murderous

Malware,

and

It’s

Spreading.”

MIT

Technology

Review,

August

22,

2019.

https://www.technologyreview.com/2019/03/05/103328/cybersecurity-critical-infrastructure-triton-m
alware.

Good,

I.

J.

"Speculations

Concerning

the

First

Ultraintelligent

Machine."

1965.

https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0065245808604180?via%3Di
hub

Greenblatt,

Ryan.

"An

Overview

of

Areas

of

Control

Work."

Alignment

Forum,

April

9,

2025.

https://www.alignmentforum.org/posts/Eeo9NrXeotWuHCgQW/an-overview-of-areas-of-control-wor
k.

Greenblatt,

Ryan,

Buck

Shlegeris,

Kshitij

Sachan,

and

Fabien

Roger.

“AI

Control:

Improving

Safety

Despite

Intentional

Subversion.”

arXiv,

July

23,

2023.

https://arxiv.org/abs/2312.06942.

Greenblatt,

Ryan,

Carson

Denison,

Benjamin

Wright,

et

al.

“Alignment

Faking

in

Large

Language

Models.”

arXiv,

December

18,

2024.

https://arxiv.org/abs/2412.14093.

Grunewald,

Erich

and

Asher

Brass

Gershovich.

“Accelerating

AI

Data

Center

Security.”

Institute

for

AI

Policy

and

Strategy,

September

2025.

https://static1.squarespace.com/static/64edf8e7f2b10d716b5ba0e1/t/68c025315a42f85b8206c46
5/1757422897410/Accelerating+AI+Data+Center+Security.pdf.

Guardiola

Múzquiz,

Gorka,

Juan

González-Gómez,

and

Enrique

Soriano-Salvador.

"The

Reverse

File

System:

Towards

Open

Cost-Eﬀective

Secure

WORM

Storage

Devices

for

Logging."

Computers

&

Security,

December

5,

2025.

https://doi.org/10.1016/j.cose.2025.104786.

AI

INTEGRITY

|

40

Halstead,

John

and

Luca

Righetti.

“Assessing

The

Risk

Of

AI-Enabled

Computer

Worms.”

GovAI,

September

10,

2025.

https://www.governance.ai/research-paper/assessing-the-risk-of-ai-enabled-computer-worms.

He,

Jiaming,

Wenbo

Jiang,

Guanyu

Hou,

Wenshu

Fan,

Rui

Zhang,

and

Hongwei

Li.

“Watch

Out

for

Your

Guidance

on

Generation!

Exploring

Conditional

Backdoor

Attacks

against

Large

Language

Models.”

arXiv,

January

8,

2024.

https://arxiv.org/abs/2404.14795.

Hubinger,

Evan,

Carson

Denison,

Jesse

Mu,

et

al.

“Sleeper

Agents:

Training

Deceptive

LLMs

That

Persist

Through

Safety

Training.”

arXiv,

January

17,

2024.

https://arxiv.org/abs/2401.05566.

Intelligence

Advanced

Research

Projects

Activity.

"TrojAI:

Trojans

in

Artiﬁcial

Intelligence."

https://www.iarpa.gov/research-programs/trojai.

Kalai,

Adam

Tauman,

Yael

Tauman

Kalai,

and

Or

Zamir.

"Consensus

Sampling

for

Safer

Generative

AI."

arXiv,

November

13,

2025.

https://doi.org/10.48550/arXiv.2511.09493.

Kastner,

Alex.

“How

an

AI

Company

CEO

Could

Quietly

Take

Over

the

World.”

AI

Futures

Project

(Substack),

October

21,

2025.

https://blog.ai-futures.org/p/how-an-ai-company-ceo-could-quietly.

Kwa,

Thomas,

Ben

West,

Joel

Becker,

et

al.

“Measuring

AI

Ability

to

Complete

Long

Tasks.”

arXiv,

March

30,

2025.

https://arxiv.org/abs/2503.14499.

Laine,

Rudolf,

Bilal

Chughtai,

Jan

Betley,

et

al.

“Me,

Myself,

and

AI:

The

Situational

Awareness

Dataset

(SAD)

for

LLMs.”

arXiv,

July

5,

2024.

https://arxiv.org/abs/2407.04694.

Larson,

Jacob,

James

S.

Denford,

Gregory

S.

Dawson,

and

Kevin

C.

Desouza.

“The

Evolution

of

Artiﬁcial

Intelligence

(AI)

Spending

by

the

U.S.

Government.”

Brookings,

March

26,

2024.

https://www.brookings.edu/articles/the-evolution-of-artiﬁcial-intelligence-ai-spending-by-the-u-s-gov
ernment/.

MacDiarmid,

Monte,

Timothy

Maxwell,

Nicholas

Scheifer,

et

al.

“Simple

Probes

Can

Catch

Sleeper

Agents.”

Anthropic,

April

23,

2024.

https://www.anthropic.com/research/probes-catch-sleeper-agents.

Martelle,

Michael,

ed.

"Eligible

Receiver

97:

Seminal

DOD

Cyber

Exercise

Included

Mock

Terror

Strikes

and

Hostage

Simulations."

National

Security

Archive,

August

1,

2018.

https://nsarchive.gwu.edu/brieﬁng-book/cyber-vault/2018-08-01/eligible-receiver-97-seminal-dod-c
yber-exercise-included-mock-terror-strikes-hostage-simulations.

McLean,

Bethany

and

Peter

Elkind.

The

Smartest

Guys

in

the

Room:

The

Amazing

Rise

and

Scandalous

Fall

of

Enron,

2004.

National

ISACs.

“National

Council

of

ISACs.”

Accessed

December

19,

2025.

https://www.nationalisacs.org/.

Nevo,

Sella,

Dan

Lahav,

Ajay

Karpur,

Yogev

Bar-On,

Henry

Alexander

Bradley,

and

Jeﬀ

Alstott.

“Securing

AI

Model

Weights.”

Rand,

May

30,

2024.

https://www.rand.org/pubs/research_reports/RRA2849-1.html.

Newport,

Annie

and

Nina

Jankowicz.

“Russian

Networks

Flood

the

Internet

with

Propaganda,

Aiming

to

Corrupt

AI

Chatbots.”

Bulletin

of

the

Atomic

Scientists,

March

27,

2025.

https://thebulletin.org/2025/03/russian-networks-ﬂood-the-internet-with-propaganda-aiming-to-corr
upt-ai-chatbots/.

Novet,

Jordan.

“Satya

Nadella

Says

As

Much

as

30%

of

Microsoft

Code

Is

Written

by

AI.”

CNBC,

April

29,

2025.

https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is
-written-by-ai.html.

OpenAI.

“Deﬁning

and

Evaluating

Political

Bias

in

LLMs.”

2025a.

https://openai.com/index/deﬁning-and-evaluating-political-bias-in-llms/.

AI

INTEGRITY

|

41

–

–

–

“OpenAI

Model

Spec.”

2025b.

https://model-spec.openai.com/2025-10-27.html.

Ottun,

Abdul-Rasheed,

Adeyinka

Akintola,

Mohan

Liyanage,

et

al.

"AI

Robustness

against

Attacks

in

City-Scale

Autonomous

Drone

Deployments."

Computer,

December

1,

2024.

https://doi.org/10.1109/MC.2024.3461841.

Pichai,

Sundar.

“Q3

Earnings

Call:

CEO’s

Remarks.”

Google,

October

29,

2024.

https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/#full-stack-approach.

Putz,

Benedikt,

Florian

Menges,

and

Günther

Pernul.

"A

Secure

and

Auditable

Logging

Infrastructure

Based

on

a

Permissioned

Blockchain."

Computers

&

Security,

November

2019.

https://doi.org/10.1016/j.cose.2019.101602.

Ron,

Javier,

Diogo

Gaspar,

Javier

Cabrera-Arteaga,

et

al.

"Galápagos:

Automated

N-Version

Programming

with

LLMs."

arXiv,

October

28,

2025.

https://arxiv.org/abs/2408.09536.

Scale

AI.

“Data

Engine.”

Accessed

December

19,

2025.

https://scale.com/data-engine.

Schoen,

Bronson,

Evgenia

Nitishinskaya,

Mikita

Balesni,

et

al.

“Stress

Testing

Deliberative

Alignment

for

Anti-Scheming

Training.”

arXiv,

September

19,

2025.

https://www.arxiv.org/abs/2509.15541.

Shavit,

Yonadav.

"What

Does

It

Take

to

Catch

a

Chinchilla?

Verifying

Rules

on

Large-Scale

Neural

Network

Training

via

Compute

Monitoring."

arXiv,

March

20,

2023.

https://arxiv.org/abs/2303.11341.

SL5

Task

Force.

“SL5

Task

Force

-

Security

Level

5

for

Frontier

AI.”

Accessed

December

19,

2025.

https://sl5.org/.

Souly,

Alexandra,

Javier

Rando,

Ed

Chapman,

et

al.

“A

Small

Number

of

Samples

Can

Poison

LLMs

of

Any

Size.”

Anthropic,

2025a.

https://www.anthropic.com/research/small-samples-poison.

–

–

–

“Poisoning

Attacks

on

LLMs

Require

a

Near-Constant

Number

of

Poison

Samples.”

arXiv,

2025b.

https://arxiv.org/abs/2510.07192.

Wei,

Bowen,

Yuan

Shen

Tay,

Howard

Liu,

et

al.

"CORTEX:

Collaborative

LLM

Agents

for

High-Stakes

Alert

Triage."

arXiv,

September

30,

2025.

https://doi.org/10.48550/arXiv.2510.00311.

The

White

House.

“FACT

SHEET:

Executive

Order

Promoting

Private

Sector

Cybersecurity

Information

Sharing.”

February

12,

2015.

https://obamawhitehouse.archives.gov/the-press-oﬃce/2015/02/12/fact-sheet-executive-order-pro
moting-private-sector-cybersecurity-inform.

The

White

House.

“Preventing

Woke

AI

in

the

Federal

Government.”

2025a

https://www.whitehouse.gov/presidential-actions/2025/07/preventing-woke-ai-in-the-federal-govern
ment/.

–

–

–

“Winning

the

Race:

America’s

AI

Action

Plan.”

2025b.

https://www.whitehouse.gov/wp-content/uploads/2025/07/Americas-AI-Action-Plan.pdf.

U.S.

Army

Cyber

Command,

“Zero

Trust.”

March

14,

2023.

https://www.army.mil/article/264818/zero_trust.

U.S.

Department

of

Defense,

“Defense

Industrial

Base

Cybersecurity

Strategy

2024.”

March

21,

2024.

https://dodcio.defense.gov/Portals/0/Documents/Library/DIB-CS-Strategy.pdf.

U.S.

Department

of

Justice.

“Volkswagen

to

Spend

Up

to

$14.7

Billion

to

Settle

Allegations

of

Cheating

Emissions

Tests

and

Deceiving

Customers

on

2.0

Liter

Diesel

Vehicles.”

June

28,

2016.

https://www.justice.gov/archives/opa/pr/volkswagen-spend-147-billion-settle-allegations-cheating-e
missions-tests-and-deceiving.

U.S.

Environmental

Protection

Agency.

“Learn

About

Volkswagen

Violations.”

March

19,

2025.

https://www.epa.gov/vw/learn-about-volkswagen-violations.

xAI.

“Grok

4.”

July

9,

2025.

https://x.ai/news/grok-4.

AI

INTEGRITY

|

42

Yu,

Miao,

Zhenhong

Zhou,

Moayad

Aloqaily,

et

al.

"Backdoor

Attribution:

Elucidating

and

Controlling

Backdoors

in

Language

Models."

arXiv,

September

30,

2025.

https://doi.org/10.48550/arXiv.2509.21761.

AI

INTEGRITY

|

43
