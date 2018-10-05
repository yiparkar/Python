import datetime
from typing import List

from data.bookings import Booking
from data.cages import Cage
from data.owners import Owner


def create_account(name: str, email: str) -> Owner:
    owner = Owner()
    owner.name = name
    owner.email = email

    owner.save()
    return owner


def find_account_by_email(email: str) -> Owner:
    owner = Owner.objects().filter(email=email).first()
    return owner


def register_cage(active_account : Owner, name, allow_dangerous, has_toys, carpeted, meters, price) -> Cage:
    cage = Cage()
    cage.name = name
    cage.has_toys = has_toys
    cage.is_carpeted = carpeted
    cage.allow_dangerous_snakes = allow_dangerous
    cage.square_meters = meters
    cage.price = price
    cage.save()

    account = find_account_by_email(active_account.email)

    account.cage_ids.append(cage.id)
    account.save()

    return cage


def find_cages_for_account(account:Owner) -> List[Cage]:
    query = Cage.objects(id__in=account.cage_ids)
    cages=list(query)

    return cages


def add_available_date(selected_cage: Cage, start_date: datetime.date, days: int) -> Cage:
    booking = Booking()
    booking.check_in_date = start_date
    booking.check_out_date = start_date + datetime.timedelta(days=days)

    cage = Cage.objects(id=selected_cage.id).first()
    cage.bookings.append(booking)
    cage.save()

    return cage