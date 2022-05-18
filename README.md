# GoScan
## ABOUT
GoScan is a red teaming tool to get inteligence from a company.
I make this as an university project from learn Go and red teaming OSINT.

## USAGE

### To get ASN and IP ranges

```
./goScan --mode SA --target TLD
```

### To get domains and subdomains

From ip_ranges.csv

```
./goScan --mode SO --target TLD
```

From sonar API

```
./goScan --mode RE --target TLD
```

### TCP scan to all domains in domains.csv

```
./goScan --mode MS --target TLD
```

## TO DO

- Remake the structure
- Add more APIs
- Improve all modes
