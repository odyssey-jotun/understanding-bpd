# -*- coding: utf-8 -*-
# Guide four: written to the teenager whose parent has BPD.
# House rules that apply here and not to the older three: no small-caps eyebrows,
# no bold lead-ins, no em dashes, no "get", second person throughout.

TRAITS_SVG = """
<figure class="diagram">
<svg viewBox="0 0 680 150" role="img"
     aria-label="Two rows of nine numbered circles, one row per parent. Each parent has five circles filled. The only circle filled in both rows is number six, which is highlighted.">
  <text x="0" y="18" class="dg-head">Same diagnosis, one trait in common</text>
  <rect x="437" y="36" width="46" height="102" rx="9" fill="#A8432A" fill-opacity="0.10"/>
  <text x="0" y="66" class="dg-lab-b">Parent A</text>
  <text x="0" y="116" class="dg-lab-b">Parent B</text>
  %s
</svg>
<figcaption>Each circle is one trait from the list above. Both parents qualify for the
diagnosis, and the only trait they share is number six. Five or more out of nine can be
met in 256 different ways.</figcaption>
</figure>
"""

def _traits():
    a = {1, 2, 3, 6, 8}
    b = {4, 5, 6, 7, 9}
    out = []
    for row, (y, s) in enumerate(((62, a), (112, b))):
        for i in range(1, 10):
            x = 150 + (i - 1) * 62
            if i in s:
                fill = "#A8432A" if i == 6 else "#2A3352"
                out.append('<circle cx="%d" cy="%d" r="17" fill="%s"/>' % (x, y, fill))
                out.append('<text x="%d" y="%d" text-anchor="middle" class="dg-num">%d</text>'
                           % (x, y + 4.5, i))
            else:
                out.append('<circle cx="%d" cy="%d" r="16.3" fill="none" stroke="#1F2233" '
                           'stroke-opacity="0.22" stroke-width="1.4"/>' % (x, y))
                out.append('<text x="%d" y="%d" text-anchor="middle" class="dg-muted">%d</text>'
                           % (x, y + 3.5, i))
    return TRAITS_SVG % "\n  ".join(out)


def _arc(cx, cy, r, fill):
    return ('<path d="M%d,%d A%d,%d 0 0 1 %d,%d Z" fill="%s"/>'
            % (cx - r, cy, r, r, cx + r, cy, fill))

def _corner():
    cx, cy = 200, 232
    rings = (_arc(cx, cy, 190, "#C3C8D7") + _arc(cx, cy, 135, "#74809C")
             + _arc(cx, cy, 80, "#465478") + _arc(cx, cy, 42, "#2A3352"))
    return """
<figure class="diagram compact">
<svg viewBox="0 0 680 250" role="img"
     aria-label="Three half-rings around the word You. The inner ring is people you see every week, the middle ring is people you could call, the outer ring is professionals. Blank lines at the right are for writing names in.">
  <text x="0" y="18" class="dg-head">Who is in your corner?</text>
  %s
  <text x="%d" y="%d" text-anchor="middle" class="dg-num">You</text>
  <text x="%d" y="182" text-anchor="middle" class="dg-lab-w">Every week</text>
  <text x="%d" y="128" text-anchor="middle" class="dg-lab-w">Could call</text>
  <text x="%d" y="74"  text-anchor="middle" class="dg-lab-b">Professionals</text>

  <circle cx="426" cy="56" r="6" fill="#465478"/>
  <text x="440" y="60" class="dg-lab-b">People I see every week</text>
  <line x1="420" y1="90"  x2="676" y2="90"  class="dg-axis"/>
  <line x1="420" y1="116" x2="676" y2="116" class="dg-axis"/>

  <circle cx="426" cy="146" r="6" fill="#74809C"/>
  <text x="440" y="150" class="dg-lab-b">People I could call</text>
  <line x1="420" y1="180" x2="676" y2="180" class="dg-axis"/>

  <circle cx="426" cy="210" r="6" fill="#C3C8D7"/>
  <text x="440" y="214" class="dg-lab-b">Professionals</text>
  <text x="440" y="232" class="dg-lab">School counselor, a doctor, 988</text>
</svg>
<figcaption>Fill this in with a pencil. One name in the inner ring is a strong start.</figcaption>
</figure>
""" % (rings, cx, cy - 12, cx, cx, cx)


JOBS_SVG = """
<figure class="diagram compact">
<svg viewBox="0 0 680 206" role="img"
     aria-label="Two columns. The left column lists jobs that belong to an adult. The right column, highlighted, lists jobs that belong to you.">
  <text x="0" y="18" class="dg-head">Whose job is it?</text>
  <rect x="2"   y="32" width="326" height="172" rx="8" fill="none" stroke="#1F2233" stroke-opacity="0.22"/>
  <rect x="352" y="32" width="326" height="172" rx="8" fill="#A8432A" fill-opacity="0.10" stroke="#A8432A" stroke-width="1.6"/>
  <rect x="2"   y="32" width="326" height="30" rx="8" fill="#1F2233" fill-opacity="0.07"/>
  <rect x="352" y="32" width="326" height="30" rx="8" fill="#A8432A"/>
  <text x="165" y="52" text-anchor="middle" class="dg-lab-b">An adult&#8217;s job</text>
  <text x="515" y="52" text-anchor="middle" class="dg-lab-w">Your job</text>
  <g class="dg-lab">
    <text x="20" y="86">Calming your parent down every night</text>
    <text x="20" y="108">Keeping the peace between your parents</text>
    <text x="20" y="130">Running the house</text>
    <text x="20" y="152">Being the one your parent tells everything</text>
    <text x="20" y="174">Deciding whether your parent needs treatment</text>

    <text x="370" y="86">School and homework</text>
    <text x="370" y="108">Friends, practice, the things you love</text>
    <text x="370" y="130">Sleep</text>
    <text x="370" y="152">Telling an adult when things are bad</text>
    <text x="370" y="174">Asking for help for yourself</text>
  </g>
</svg>
<figcaption>If the left column sounds like your week, tell your steady adult. Handing one of
those jobs back to a grown-up is a real change.</figcaption>
</figure>
"""


BODY = """

<section class="block loose">
  <h2>Questions you've probably asked</h2>
  <div class="rule"></div>
  <p class="lede">Why is my parent fine one minute and furious the next?</p>
  <p class="lede">Did I do something to cause this?</p>
  <p class="lede">Is it always going to be like this?</p>
  <p>Honestly, these are the questions I wish someone had answered for me a lot sooner. They
  sound simple, but most kids carry them around for years without ever saying them out
  loud.</p>
  <p>If one of your parents, another family member, or someone you love has BPD, or you think they might, I wrote this for you. Most of what's
  out there about BPD is written for the person who has it, or for their partner. Very
  little is written for the kid down the hall, even though somewhere between 17 and 25
  percent of kids worldwide live with at least one parent who has a mental illness (Van
  Schoors and colleagues, 2023). You are definitely not the only one. Everything in here
  comes from research I spent the summer digging through, plus what I learned by living
  it.</p>
  <div class="callout">
    <p class="lead">If someone is in danger right now</p>
    <p>Call or text 988, any hour of the day. If someone could die, call 911. More numbers
    are near the end of this guide.</p>
  </div>
</section>

<section class="block loose">
  <h2>What is BPD, in plain words?</h2>
  <div class="rule"></div>
  <p>Borderline personality disorder is a mental illness that affects how a person handles
  their emotions. Feelings hit faster and harder, and they take longer to fade than they do
  for most people. Relationships feel really high-stakes, because the person is often
  terrified of being left.</p>
  <p>Doctors diagnose it from a list of nine traits, and a person needs five or more. I think it
  helps to see the actual list, because most people only know BPD from TV or TikTok, and
  the real thing looks a lot different.</p>
  <ol class="crit traits cols2" style="break-inside:avoid-page">
    <li>Working hard to avoid being left, even when nobody is leaving.</li>
    <li>Relationships that swing between adoring someone and resenting them.</li>
    <li>A shaky sense of who they are.</li>
    <li>Impulsive choices that can hurt them, like overspending or reckless driving.</li>
    <li>Self-harm, or threats or attempts of suicide.</li>
    <li>Moods that change fast, often within hours.</li>
    <li>A long-lasting feeling of emptiness.</li>
    <li>Intense anger that's hard to control.</li>
    <li>Under heavy stress, feeling paranoid or unreal.</li>
  </ol>
%(traits)s
  <p>So your parent has their own version of BPD. The way to understand it is to learn their
  patterns: what sets them off, how long it lasts, and what helps them calm back down.</p>
</section>

<section class="block loose">
  <h2>Why does my parent seem like two different people?</h2>
  <div class="rule"></div>
  <p>One day your parent is the most fun person you know. The next day you're walking on
  eggshells. The day after that, they act like nothing happened. If you've ever wondered which
  one is the real them, you're not alone.</p>
  <p>Researchers who study parents with BPD describe the same pattern. A parent can swing
  between two modes (Stepp and colleagues, 2012). In one, they're controlling and harsh:
  criticizing you, checking up on you, angry about small things. In the other, they pull
  away and become distant and hard to reach.</p>
  <p>A lot of kids decide one of these is the real parent and the other is an act. Honestly,
  both are real. Both come from the same illness, and neither one is a verdict on you.</p>
  <p>BPD also makes people see others in all-or-nothing terms. On Monday you're the only one
  who understands them. On Tuesday you're selfish and ungrateful. You stayed the same person
  between Monday and Tuesday. Their view of you swung, and it will probably swing back.</p>
</section>

<section class="block loose">
  <h2>Did I cause this?</h2>
  <div class="rule"></div>
  <p class="lede">No. There's a saying from Al-Anon, a support group for families, that fits
  here too: you didn't cause it, you can't control it, and you can't cure it.</p>
  <p>BPD grows out of a mix of genes and life experience, usually long before a person has
  kids. Nothing you said at dinner caused it, and no amount of perfect behavior will fix
  it.</p>
  <h3>How understanding the illness helps you</h3>
  <p>Of course, understanding an illness won't make it go away, and it won't make every hard
  day easier. Still, I really believe it's the most useful thing in this guide, and the
  research agrees. A review of 37 studies
  found that kids whose parent has a mental illness do better when someone explains the
  illness in words they can follow (Van Schoors and colleagues, 2023). In programs that
  taught kids about a parent's illness, kids were about a third as likely to develop
  depression or anxiety over the next year or so (Havinga and colleagues, 2021). Those
  programs were for parents with depression or anxiety, and research on BPD families is
  newer. Still, understanding is the best place to start.</p>
  <div class="side short">
    <figure>
      <img src="img/g4-journal.jpg" alt="A teenage girl writing in a notebook at a table by a sunny window">
    </figure>
    <div class="text">
      <p>Here's what changes once you understand it.</p>
      <ul>
        <li>You stop taking the blame. A blowup becomes a symptom you can name.</li>
        <li>Your parent becomes more predictable. You learn the triggers and roughly how long
        a bad stretch lasts.</li>
        <li>You have words for it. &ldquo;My parent has an illness called BPD&rdquo; is a
        sentence you can say to a counselor or a friend.</li>
        <li>You can see the person underneath. Your parent is more than their worst
        days.</li>
      </ul>
    </div>
  </div>
</section>

<section class="block loose">
  <h2>What tends to set things off?</h2>
  <div class="rule"></div>
  <p>The biggest trigger is fear of being left. People with BPD watch closely for signs that
  someone is pulling away, and they react hard when they think they see one.</p>
  <p>That puts teenagers in a tough spot, because growing up means pulling away a little. You
  close your door, you want time with friends, you keep some things private. All of that is
  normal. To a parent with BPD, each one can feel like the first step toward being abandoned.
  No study has tested this exact point, but it follows from how the illness works, and it
  explains a lot of fights that seem to come out of nowhere.</p>
  <p>Sometimes the trigger is tiny. A forgotten chore or the wrong tone of voice can
  hang over the house for days. Knowing the pattern won't stop the reaction. It does mean you can see it
  coming and choose how you respond. These example conversations aren't from a study, so
  put them in your own words.</p>

  <div class="script plain">
    <p class="sit">You're heading out with friends and your parent is upset</p>
    <div class="line no"><span class="tag">Instead of</span>
      <p class="say">&ldquo;Why do you always do this? I'm allowed to have a life.&rdquo;</p></div>
    <div class="line yes"><span class="tag">Try</span>
      <p class="say">&ldquo;I'm going to Maya's until nine. I'll text you from there, and I'll
      be home at nine.&rdquo;</p></div>
    <p class="why">A set time and a promise to check in speak to the fear underneath. An
    argument about your rights skips right past it.</p>
  </div>

  <div class="script plain">
    <p class="sit">Your parent says you don't love them</p>
    <div class="line no"><span class="tag">Instead of</span>
      <p class="say">&ldquo;That's ridiculous. You're being crazy.&rdquo;</p></div>
    <div class="line yes"><span class="tag">Try</span>
      <p class="say">&ldquo;I do love you. I can tell you're really scared right now.&rdquo;</p></div>
    <p class="why">While the feeling is this strong, arguing the facts goes nowhere. Naming
    the feeling usually lowers the temperature.</p>
  </div>

  <div class="script plain">
    <p class="sit">Your parent goes silent after an argument</p>
    <div class="line no"><span class="tag">Instead of</span>
      <p class="say">Following them from room to room until they talk.</p></div>
    <div class="line yes"><span class="tag">Try</span>
      <p class="say">&ldquo;I'm going to do my homework. I'm here when you want to talk.&rdquo;</p></div>
    <p class="why">You can't pull someone out of a shutdown. Telling them where you are, and
    that you're staying, is enough.</p>
  </div>
</section>

<section class="block loose">
  <h2>What can I actually do?</h2>
  <div class="rule"></div>
  <p class="lede">More than you might think. Research on kids whose parent has a mental
  illness keeps finding the same few things that protect them, and you can start most of
  them this week.</p>

  <h3>Pick one steady adult</h3>
  <p>Your steady adult could be your other parent, a grandparent, an aunt or uncle, a coach, a teacher or your
  school counselor. Who it is matters less than how often you see them, because support that
  shows up regularly makes the biggest difference (Van Schoors and colleagues, 2023). The same
  review found that being close with a brother or sister protects kids too, so if you have
  one, look out for each other.</p>
%(corner)s
  <h3>Keep your own life going</h3>
  <figure class="band">
    <img src="img/g4-friends.jpg" alt="Three teenage girls laughing together outdoors">
  </figure>
  <p>When researchers asked kids in your position what helped, they named time with friends
  and ordinary activities (Bee and colleagues, 2014). Kids who coped by accepting what they
  couldn't change, looking for the good in things and taking their mind off it had less
  anxiety and depression (Van Schoors and colleagues, 2023). The ordinary
  stuff counts: practice, a sleepover, an afternoon doing absolutely nothing with your
  friends. You're allowed to have a good time while things at home are hard.</p>

  <h3>Tell one safe person</h3>
  <p>Kids with a parent who has a mental illness often keep it a secret, because they're
  afraid of being laughed at or teased (Dobener and colleagues, 2022). Carrying
  that alone wears you down. You don't need to tell everyone. One safe person is enough: a
  friend you trust, a relative, a counselor. In one review, kids said talking to someone
  helped even when the conversation wasn't about their parent at all, and one girl said
  talking to her pet made her feel better (Sawitzki and colleagues, 2025).</p>
  <figure class="band">
    <img src="img/g4-counselor.jpg" alt="A teenage girl talking with a counselor in a bright, calm office">
    <figcaption>A school counselor is a good first choice. Talking with students about hard
    things at home is part of the job.</figcaption>
  </figure>
</section>

<section class="block loose">
  <h2>Have I become the parent?</h2>
  <div class="rule"></div>
  <p>Maybe you're the one who makes sure dinner happens. Maybe you're the one who calms
  everybody down, or the one your parent vents to about the other adults in their life. At
  the time, it just feels like being responsible.</p>
  <p>Researchers have a name for it: role reversal. In a review of 14 studies, young people
  with a parent who had a mental illness described taking over their parent's job so often
  that the researchers had to add a new category to the standard model of how kids cope
  (Sawitzki and colleagues, 2025). Kids who do this are often praised for being mature. Of
  course, it's still too much weight for someone your age.</p>
%(jobs)s
</section>

<section class="block loose">
  <h2>Should I try to talk my parent into therapy?</h2>
  <div class="rule"></div>
  <p class="lede">You can, and you can also leave it to an adult. Your parent's treatment is
  their responsibility and their doctor's.</p>
  <p>If you do bring it up, research on adults gives a few clues. People who were listened to
  without judgment and gently pointed toward help were much more likely to see a doctor or
  therapist afterward (Morgan and colleagues, 2025). Almost half of people who skip treatment
  don't think they need it, and most of the rest want to handle it on their own (Mojtabai
  and colleagues, 2011), so one conversation rarely settles it. In one study, parents with BPD said they wanted help
  being better parents (Zalewski and colleagues, 2015). That's usually a better way in than
  the word &ldquo;disorder.&rdquo;</p>

  <div class="script plain">
    <p class="sit">Bringing it up for the first time</p>
    <div class="line no"><span class="tag">Instead of</span>
      <p class="say">&ldquo;You need help. I looked it up, and I think you have BPD.&rdquo;</p></div>
    <div class="line yes"><span class="tag">Try</span>
      <p class="say">&ldquo;I love you, and I can see how hard things have been. Would you
      talk to someone? I'd feel better knowing you had support.&rdquo;</p></div>
    <p class="why">A diagnosis from your own kid lands as an accusation. Worry from your own
    kid is much harder to argue with.</p>
  </div>

  <div class="script plain">
    <p class="sit">In the middle of a fight</p>
    <div class="line no"><span class="tag">Instead of</span>
      <p class="say">&ldquo;If you don't go to therapy, you're going to lose us.&rdquo;</p></div>
    <div class="line yes"><span class="tag">Try</span>
      <p class="say">Saying nothing about therapy until you're both calm.</p></div>
    <p class="why">About one in five parents in one study of public mental health care
    feared losing custody of their kids over treatment (Busch and Redlich, 2007). A threat
    feeds that fear and makes treatment less likely.</p>
  </div>

  <p>I'll be honest: some people never go, no matter how the subject comes up. A trusted adult can carry this conversation better than you can. In research
  trials, a short family session where a counselor explains the illness to everyone helped
  kids feel less anxious (Solantaus and colleagues, 2010). Ask your steady adult whether your
  parent's therapist, or a counselor, could set one up.</p>
</section>

<section class="block">
  <h2>When home doesn't feel safe</h2>
  <div class="rule"></div>
  <p>Understanding the illness helps you make sense of your parent's behavior. Being hurt is
  still never okay. If a parent hits you, threatens you, or leaves you without food or a safe
  place to sleep, tell an adult you trust or call one of these numbers. What happens next,
  including where you stay, is something to work out with that adult.</p>
  <div class="crisis">
    <h3>Free, confidential, and open all day and night</h3>
    <ul>
      <li>988 Suicide &amp; Crisis Lifeline: call or text 988. You can call about your parent
      or about yourself.</li>
      <li>Childhelp National Child Abuse Hotline: call or text 1-800-422-4453.</li>
      <li>Crisis Text Line: text HOME to 741741.</li>
      <li>If anyone is in immediate danger, call 911.</li>
    </ul>
  </div>
</section>

<section class="block">
  <h2>Where to start this week</h2>
  <div class="rule"></div>
  <p>Five small steps. None of them depend on your parent changing.</p>
  <ul class="check">
    <li>Write one name in the inner ring of your corner.</li>
    <li>Tell that person one true thing about what happens at home.</li>
    <li>Make one plan with friends, and keep it.</li>
    <li>Pick one job from the adult column and hand it back to a grown-up.</li>
    <li>Save 988 and 1-800-422-4453 in your phone.</li>
  </ul>
</section>

<section class="block loose">
  <h2>Will my parent ever recover?</h2>
  <div class="rule"></div>
  <div class="side">
    <figure>
      <img src="img/g4-braid.jpg" alt="A mother braiding her teenage daughter's hair on a sunny staircase, both relaxed">
    </figure>
    <div class="text">
      <p class="lede">There's real reason for hope.</p>
      <p>A review of 19 long-term studies found that remission from BPD, meaning a person no
      longer meets the criteria, is common. Once people reach remission, few slip back (Ng
      and colleagues, 2016). Treatments like dialectical behavior therapy, or DBT, were built
      specifically for BPD.</p>
      <p>Recovery in everyday life, like steady relationships and work, can take longer than
      the symptoms do. Not everyone with BPD looks for help. If your parent never does,
      you can still love them and still look after yourself. Plenty of parents do recover,
      though, and families change with them.</p>
    </div>
  </div>
  <p>Your own future belongs to you, too. Understanding the illness, a steady adult, friends,
  and your own ways of coping are the same things researchers link to kids doing well when a
  parent is unwell (Van Schoors and colleagues, 2023). In one study, several adults who grew
  up with a parent's mental illness went on to helping careers like counseling and social
  work (Patrick and colleagues, 2019). I don't think that's a
  coincidence. Growing up like this teaches you a lot about people, and what you do with that
  is up to you.</p>
  <figure class="band" style="margin-top:16pt">
    <img src="img/g4-reading.jpg" alt="Two teenage girls lying on a bed, smiling over a book and a tablet">
  </figure>
</section>

""" % {"traits": _traits(), "corner": _corner(), "jobs": JOBS_SVG}

REFS = [
 'American Psychiatric Association. (2022). <em>Diagnostic and Statistical Manual of Mental Disorders</em> (5th ed., text rev.). The nine traits are paraphrased from the criteria for borderline personality disorder.',
 'Stepp, S. D., Whalen, D. J., Pilkonis, P. A., Hipwell, A. E., &amp; Levine, M. D. (2012). Children of mothers with borderline personality disorder: identifying parenting behaviors as potential targets for intervention. <em>Personality Disorders: Theory, Research, and Treatment, 3</em>(1), 76-91. pmc.ncbi.nlm.nih.gov/articles/PMC3268672/',
 'Van Schoors, M., Van Lierde, E., Steeman, K., Verhofstadt, L. L., &amp; Lemmens, G. M. D. (2023). Protective factors enhancing resilience in children of parents with a mental illness: a systematic review. <em>Frontiers in Psychology, 14</em>, 1243784. doi.org/10.3389/fpsyg.2023.1243784',
 'Havinga, P. J., Maciejewski, D. F., Hartman, C. A., Hillegers, M. H. J., Schoevers, R. A., &amp; Penninx, B. W. J. H. (2021). Prevention programmes for children of parents with a mood/anxiety disorder: systematic review of existing programmes and meta-analysis of their efficacy. <em>British Journal of Clinical Psychology, 60</em>(2), 212-251. doi.org/10.1111/bjc.12277',
 'Bee, P., Bower, P., Byford, S., et al. (2014). The clinical effectiveness, cost-effectiveness and acceptability of community-based interventions aimed at improving or maintaining quality of life in children of parents with serious mental illness: a systematic review. <em>Health Technology Assessment, 18</em>(8). doi.org/10.3310/hta18080',
 'Dobener, L.-M., Fahrer, J., Purtscheller, D., Bauer, A., Paul, J. L., &amp; Christiansen, H. (2022). How do children of parents with mental illness experience stigma? A systematic mixed studies review. <em>Frontiers in Psychiatry, 13</em>, 813519. doi.org/10.3389/fpsyt.2022.813519',
 'Sawitzki, M., Kinzenbach, S., Christiansen, H., &amp; Grossheinrich, N. (2025). Systematic review and meta-synthesis: coping strategies of children, adolescents, and young adults of parents with a mental illness. <em>Clinical Child and Family Psychology Review.</em> doi.org/10.1007/s10567-025-00540-8',
 'Morgan, A. J., Wright, J., Mackinnon, A. J., Reavley, N. J., Rossetto, A., Le, L. K.-D., &amp; Jorm, A. F. (2025). Receiving support for mental health problems from family and friends: measurement and impact on mental health, relationships, and help-seeking. <em>PLOS Mental Health.</em> doi.org/10.1371/journal.pmen.0000502',
 'Mojtabai, R., Olfson, M., Sampson, N. A., et al. (2011). Barriers to mental health treatment: results from the National Comorbidity Survey Replication. <em>Psychological Medicine, 41</em>(8), 1751-1761. pmc.ncbi.nlm.nih.gov/articles/PMC3128692/',
 'Zalewski, M., Stepp, S. D., Whalen, D. J., &amp; Scott, L. N. (2015). A qualitative assessment of the parenting challenges and treatment needs of mothers with borderline personality disorder. <em>Journal of Psychotherapy Integration, 25</em>(2), 71-89. pmc.ncbi.nlm.nih.gov/articles/PMC4528980/',
 'Busch, A. B., &amp; Redlich, A. D. (2007). Patients\' perception of possible child custody or visitation loss for nonadherence to psychiatric treatment. <em>Psychiatric Services, 58</em>(7), 999-1002. pmc.ncbi.nlm.nih.gov/articles/PMC2030627/',
 'Solantaus, T., Paavonen, E. J., Toikka, S., &amp; Punam&auml;ki, R.-L. (2010). Preventive interventions in families with parental depression: children\'s psychosocial symptoms and prosocial behaviour. <em>European Child &amp; Adolescent Psychiatry, 19</em>(12), 883-892. doi.org/10.1007/s00787-010-0135-3',
 'Ng, F. Y. Y., Bourke, M. E., &amp; Grenyer, B. F. S. (2016). Recovery from borderline personality disorder: a systematic review of the perspectives of consumers, clinicians, family and carers. <em>PLoS ONE, 11</em>(8), e0160515. doi.org/10.1371/journal.pone.0160515',
 'Patrick, P. M., Reupert, A. E., &amp; McLean, L. A. (2019). &ldquo;We are more than our parents\' mental illness&rdquo;: narratives from adult children. <em>International Journal of Environmental Research and Public Health, 16</em>(5), 839. doi.org/10.3390/ijerph16050839',
 'Al-Anon Family Groups. The &ldquo;three Cs&rdquo; are a long-standing Al-Anon and Alateen saying. al-anon.org',
 'Substance Abuse and Mental Health Services Administration. <em>988 Suicide &amp; Crisis Lifeline.</em> samhsa.gov/find-help/988',
 'Childhelp. <em>National Child Abuse Hotline.</em> childhelphotline.org',
]
NOTE = ('Most of the research on programs for children studied parents with depression or '
        'anxiety; studies of children of parents with BPD are fewer and more recent. The '
        'example conversations and the three diagrams were written for this guide. They follow '
        'the research above, and they were not themselves tested in a study. Crisis numbers '
        'were checked as current at the time of writing.')

KICKER = ""
TITLE  = "When Your Parent Has BPD"
SUB    = ("What is happening at home, why you didn't cause it, and what you can do "
          "starting this week.")
IMG    = "g4-cover.jpg"


# Guide four's About page is in Marley's own voice, unlike the other three.
ABOUT_BODY = """
      <h2>Hi, I'm Marley</h2>
      <div class="rule"></div>
      <p class="name-line">I made these guides because my family needed them and nobody had
      written them yet.</p>
      <p>I grew up in a family where emotions ran high and nobody had a word for why. Once I
      finally had one, I spent a summer digging through clinical research on borderline
      personality disorder to understand what I had been living with. These guides are what
      came out of it.</p>
      <p>I'm a high school senior in Arkansas, and I want to become a psychiatrist. Every
      research claim in here is cited at the back, and the guides are free. Please share
      them with anyone who needs them.</p>
      <div class="about-quote">
        <p>&ldquo;Nobody in my family had the language for what was happening. These guides
        are the thing I wish someone had handed us.&rdquo;</p>
      </div>
"""
