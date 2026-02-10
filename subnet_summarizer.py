from netaddr import IPNetwork, IPAddress, cidr_merge, AddrFormatError
import time


class SubnetSummarizer:
    """
    A class to read, validate, summarize, and export IP subnets.

    Attributes:
        input_file  (str): Path to the file containing IP subnets.
        output_file (str): Path to the file where results are saved.
    """

    def __init__(self, input_file: str, output_file: str = 'Summarized_subnets.txt'):
        self.input_file = input_file
        self.output_file = output_file
        self._raw_subnets: list[IPNetwork] = []
        self._summarized_subnets: list[IPNetwork] = []
        self._invalid_entries: list[str] = []
        self._elapsed_time: float = 0.0

    # ------------------------------------------------------------------ #
    # Properties (read-only access to internal state)
    # ------------------------------------------------------------------ #

    @property
    def total_input(self) -> int:
        """Total number of valid subnets loaded from the input file."""
        return len(self._raw_subnets)

    @property
    def total_summarized(self) -> int:
        """Total number of subnets after CIDR summarization."""
        return len(self._summarized_subnets)

    @property
    def invalid_count(self) -> int:
        """Total number of invalid / skipped entries."""
        return len(self._invalid_entries)

    # ------------------------------------------------------------------ #
    # Public interface
    # ------------------------------------------------------------------ #

    def load(self) -> None:
        """Read subnets from the input file, skipping blank lines and invalid entries."""
        self._raw_subnets.clear()
        self._invalid_entries.clear()

        with open(self.input_file, 'r') as f:
            for line in f:
                entry = line.strip()
                if not entry:          # skip blank lines
                    continue
                try:
                    self._raw_subnets.append(IPNetwork(entry))
                except (AddrFormatError, ValueError):
                    self._invalid_entries.append(entry)
                    print(f"  ⚠  Skipping invalid entry: '{entry}'")

        print(f"Loaded {self.total_input} valid subnet(s) "
              f"({self.invalid_count} invalid skipped).")

    def summarize(self) -> None:
        """Perform CIDR merge/summarization on the loaded subnets."""
        if not self._raw_subnets:
            raise ValueError("No subnets loaded. Call load() first.")

        start = time.perf_counter()
        self._summarized_subnets = cidr_merge(self._raw_subnets)
        self._elapsed_time = time.perf_counter() - start

        print(f"Summarized {self.total_input} subnet(s) → "
              f"{self.total_summarized} subnet(s) "
              f"in {self._elapsed_time:.6f}s.")

    def save(self) -> None:
        """Write summarized subnets to the output file (overwrites existing)."""
        if not self._summarized_subnets:
            raise ValueError("No summarized subnets to save. Call summarize() first.")

        with open(self.output_file, 'w') as f:
            f.writelines(f"{subnet}\n" for subnet in self._summarized_subnets)

        print(f"Results saved to '{self.output_file}'.")

    def report(self) -> None:
        """Print a summary report to the console."""
        print("\n" + "=" * 50)
        print("        IP SUBNET SUMMARIZATION REPORT")
        print("=" * 50)
        print(f"  Input file       : {self.input_file}")
        print(f"  Output file      : {self.output_file}")
        print(f"  Total loaded     : {self.total_input}")
        print(f"  After summary    : {self.total_summarized}")
        print(f"  Reduction        : {self.total_input - self.total_summarized} subnet(s) removed")
        print(f"  Invalid skipped  : {self.invalid_count}")
        print(f"  Time taken       : {self._elapsed_time:.6f}s")
        print("=" * 50)
        print("\n  Summarized Subnets:")
        for subnet in self._summarized_subnets:
            print(f"    {subnet}")
        print()

    def run(self) -> None:
        """Convenience method: load → summarize → save → report in one call."""
        self.load()
        self.summarize()
        self.save()
        self.report()


# ------------------------------------------------------------------ #
# Entry point
# ------------------------------------------------------------------ #

if __name__ == '__main__':
    summarizer = SubnetSummarizer(
        input_file='route.txt',
        output_file='Summarized_subnets.txt'
    )
    summarizer.run()

    # --- You can also call each step individually for more control ---
    # summarizer.load()
    # summarizer.summarize()
    # summarizer.save()
    # summarizer.report()

    print("Code written by SUHAS B.")
