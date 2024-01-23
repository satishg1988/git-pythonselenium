from abhibus.pom.pages.offers import Offers


def test_verifyTextOfBusBookingsOfferHeading(setUp, expected_heading_text="Bus Booking Offers"):
    Offers(setUp).clickOffersHeaderOption()
    assert Offers(setUp).getTextOfBusBookingsOfferHeading().casefold() == expected_heading_text.casefold()


def test_verifyOfferCards(setUp, req_title="Get Upto Rs.350 Cashback",
                          expected_text = "Hello, Your Coupon Code Copied."):
    Offers(setUp).clickOffersHeaderOption()
    assert Offers(setUp).getOfferCards(req_title).text.casefold() == req_title.casefold()
    Offers(setUp).clickCopyCodeBtn()
    assert expected_text.casefold() in Offers(setUp).getTextOfCopiedCode().casefold()
