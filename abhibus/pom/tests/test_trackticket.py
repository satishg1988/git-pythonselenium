from abhibus.pom.pages.trackticket import TrackTicket


def test_verifyTextOfBusBookingsOfferHeading(setUp, expected_trackticket_heading="Enter Ticket Details"):
    TrackTicket(setUp).clickTrackTicketOption()
    assert TrackTicket(setUp).getTextOfTrackTicketHeading().casefold() == expected_trackticket_heading.casefold()


def test_errorMessageWhenBookingIdEmpty(setUp,
                                        expected_errormsg_bookingid="please enter the booking valid booking id",
                                        expected_errormsg_mobile_empty="Please provide the correct mobile number"):
    TrackTicket(setUp).clickTrackTicketOption()
    TrackTicket(setUp).clickTicketDetailsButton()
    assert TrackTicket(setUp).getErrorMsgBookingIdEmpty().casefold() == expected_errormsg_bookingid.casefold()
    assert TrackTicket(setUp).getErrorMsgMobileEmpty().casefold() == expected_errormsg_mobile_empty.casefold()
