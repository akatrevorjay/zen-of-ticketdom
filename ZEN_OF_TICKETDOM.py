
"""THE ZEN OF TICKETDOM"""

"""
         PS. THIS DOCUMENT WAS ONCE KNOWN AS:

    TIME MANAGING TICKET SYSTEMS FOR FUN AND PROFIT
          (don't slice those wrists just yet)
"""

def POINTS():
    """
    * Idea is a ticket system that integrates highly with Pomodoro.

    * Tight email integration is the Zen of Ticketdom.

    * Adhere strongly to all standards humanly (and alienly) possible.

    * KISS (Keep it simple, stupid.)

    * DRY (Don't repeat yourself.)
    """


def SYMBOLS():
    """
    # queue
    @ tag

    % customer
    $ order/part

    + watching
    * new
    ! attention / emergency
    ~ in progress
    """


def QUEUES():
    """
    * Queues are simply lists of tickets.

    * A ticket can only be in one queue at a time. (Think hashtags.)

    * (carp) Queues are also publisher/subscriber based for notifications.
    """

    def INITIAL_QUEUES():
        """
        * Each login gets their own queue, siginified as #<login>
          ie, #trevorj is my queue.

        * #incoming is the queue for new incoming tickets that have not been
          given the gift of flight yet.

        * #completed is the queue for completed tickets.

        * #hold is the queue for tickets that are 'on hold'.
        """


def TAGS():
    """
    * Tags are wonderous things that I hope that we all know,
      but for definition they are named groups.

    * Tickets can have multiple tags.

    * These are great for sorting, narrowing down data, etc.
    """

    def INITIAL_TAGS():
        """
        * @needs-info means that more information is needed for this ticket,
          ie, customer could not be guessed and it needs to be manually assigned.

        * @scheduled means that this ticket is scheduled for a later date.
          Symbol: clock

        * @complete means that this ticket is complete.
          Symbol: checkmark

        * @wip means that this ticket is in progress.
          Symbol: ~

        * @order means that this ticket has order(s) attached.
          Symbol: $

        * @attachment means that this ticket has a file (virus) attached.
          Symbol: paperclip

        * @attention means that this ticket is important (ie, emergency).
          Symbol: !

        * @new means that this ticket is new (ie, unread).
          Symbol: *
        """


def THE_LIFE_OF_BRIAN(AND, HIS, TICKET):
    """
    * Isn't it awfully nice to have a ticket?
    """

    """
    > Tickets are submitted via email.

        * Each queue gets it's own email address.

               eg: incoming@support.incognito.org --> #incoming
                   trevorj@support.incognito.org --> #trevorj (trevorj's personal queue)

               ( support@incognito.org would then be aliased to
                 incoming@support.incognito.org )

        * Each ticket gets it's own email address.

               eg: ticket-48929@support.incognito.org


    > Incoming Tickets would be emailed to support@incognito.org.
      This goes into the #incoming queue by default.

        * If possible, customer will be guessed based on From: email address.

          If it cannot guess it, it will be tagged with @needs-info so the
          dispatcher that checks the #incoming queue can apply the power of
          information cream as needed until redness and swelling is alleviated.

          Once an unknown From: email address is associated with client, this
          mapping is remembered henceforth and so on, allowing the system to
          one day become self-aware. )

        * Example:

            From: Rachel McEvans <rm@awesomeco.com>

            HALP! MY KEYBOARD JUST LIKE STOPPED WORKING LIKE ALL OF A SUDDEN AND I
            NEED IT FIXED ASAP. WHY DOES EVERYTHING ALWAYS BREAK ALL THE ITME? KTHX

        * System adds information to email text at the top in nice, easy to find, read,
          search for, data munge format:

            %% Customer: AwesomeCo
            %% Submitted: December 12th, 2012 1:51a


    > Dispatcher gets notified about ticket in 'incoming' queue.

        * awesomeco.com is in one of the domains listed for the client "AwesomeCo", so
          the system automatically attaches this ticket to the "AwesomeCo" customer.



    > Dispatcher checks information in ticket, fixes or adds as needed.
      This is done via a simple reply.

        * If @needs-info tag is set, fill in missing info that could not be guessed,
          or add any notes you may have for this ticket before it gets pushed out.


    > Dispatcher sends ticket to the next queue by means of forwarding the message
      to the new owner's queue address.

      * Since every login gets their own queue, assigning a ticket to someone is as
        simple as forwarding a message to, for instance, trevorj@support.incognito.org

      * To have others get updates for a ticket and able to add time, etc, but not be
        primary, just CC their queue address on a reply. This way everything is recorded,
        even when someone was added to a ticket. Being part of a ticket but not primary
        is known as a subscription to a ticket, ala they are subscribed to the ticket.


    > New ticket owner gets notified about new ticket in #personal queue.

      * Anyone who's subscribed to the ticket gets notified about new ticket in a less
      loud way, signifying it as not being quite as important as a new one in your
      own personal queue. As it should be.


    > New owner updates the ticket by replying to the message in his queue.

        * Message will be sent from the ticket-48473@support.incognito.org address,
          this way it's easy for the system to keep track of which updates are for which
          ticket.

        * Details of ticket are embedded in email as simple text:

            Called Rachel about issue. After speaking with her, remoting into her PC and
            troubleshooting the cable connection, we came to the conclusion that her
            keyboard was not working because she had poured slim fast into it.
            Customer was under the impression that slim fast was not conductive but
            would instead make her keyboard slimmer and have more energy in the morning.
            I explained how I didn't know that to be the case, and that I'm bringing her
            a new keyboard tomorrow morning so we can get her up and running asap.

            %% Order: Cheap @Keyboard from Microcenter = $9.99
            %% Hours: 1.5
            %% Tags: @id10t


    > To close ticket, just forward it to the completed queue address.
    """


def OH_SNAP_ITS_AN_APP():
    """
    > Extremely tiny app sits in your system tray. This is what notifies you of tickets in a
      decent manner.

    > Gets list of tickets in your queue. When you right click it it has RIGHT THERE, easy
      and quick as light access to switch ticket you're working on. One click, BAM, time
      clock is ticking for that ticket.

    > This is also a pomodoro timer. You start it by selecting a ticket in your queue.

    > Every 25m it asks you politely and out of your way, hey, are you still working on '[Client] [Ticket Title]' ? If not, change me!

    > After you inform it, it informs you you've done your duties and should take a couple
      minute break if you can so your brain doesn't fry, pomodoro style. If you do take it,
      it will let you know when to get the fuck back to work.

    > At each 30m interval, it will send a +30m notice to the ticketing system for the ticket
      you've been working on, autoincrementing your time. Like a boss.
    """
