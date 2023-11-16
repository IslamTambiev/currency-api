from fastapi import HTTPException
from pydantic import BaseModel, field_validator, model_validator

currencies_list = ['AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN',
                   'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD',
                   'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP',
                   'DZD', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF',
                   'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK',
                   'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK',
                   'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP',
                   'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR',
                   'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD',
                   'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLE', 'SLL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB',
                   'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF',
                   'VES', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMK',
                   'ZMW', 'ZWL']


class CurrencyPair(BaseModel):
    base: str
    quote: str
    amount: float

    @field_validator('base', 'quote')
    @classmethod
    def currency_check(cls, v: str) -> str:
        """
        Validates the currency value.

        Args:
            v (str): The currency value to be validated.

        Returns:
            str: The validated currency value.

        Raises:
            HTTPException: If the currency value is not valid.
                status_code (int): The status code of the exception.
                detail (str): The detail message of the exception.
        """
        if len(v) == 3 and v.isalpha() and v.upper() in currencies_list:
            return v.upper()
        else:
            raise HTTPException(
                status_code=400,
                detail='The value must be 3 characters and only letters'
            )

    @model_validator(mode='after')
    def pair_check(self) -> 'CurrencyPair':
        """
        A function that checks if the base and quote currencies are different.

        Returns:
            CurrencyPair: The CurrencyPair instance.

        Raises:
            HTTPException: If the base and quote currencies are the same.
        """
        if self.base == self.quote:
            raise HTTPException(
                status_code=400,
                detail='The currencies cannot be the same'
            )
        return self
