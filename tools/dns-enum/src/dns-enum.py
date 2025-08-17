
import time
import dns.resolver
import dns.exception

target_domain = 'youtube.com'
record_types = ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'SOA']

# Bypass /etc/resolv.conf and use known-good public resolvers
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ["1.1.1.1", "1.0.0.1", "8.8.8.8", "8.8.4.4"]
resolver.timeout = 3.0  # per-try timeout (seconds)
resolver.lifetime = 8.0     # total time per query (seconds)

for rtype in record_types:
    # Try UDP first, then TCP fallback if needed
    answers = None
    for force_tcp in (False, True):
        try:
            response = resolver.resolve(
                target_domain, rtype, tcp=force_tcp, raise_on_no_answer=False
            )
            if response.rrset:
                answers = [str(r) for r in response]
            break  # success or empty; stop retrying TCP/UDP
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            # Domain doesn't exist for this type or no records; don't treat as error
            answers = []
            break
        except (dns.resolver.LifetimeTimeout, dns.exception.Timeout, dns.resolver.NoNameservers):
            # Try TCP fallback after UDP; if already TCP, we'll report below
            if force_tcp:
                answers = None  # mark as failure after both tries
            continue

        if answers is None:
            print(f"{rtype} records for {target_domain}: (none)")
        elif not answers:
            # No records for this type (common for CNAME at the zone apex)
            print(f"{rtype} records for {target_domain}: (none)")
        else:
            print(f"{rtype} records for {target_domain}")
            for a in answers:
                print(f"  {a}")

        time.sleep(0.2)  # small pause to avoid rate limits on some resolvers
