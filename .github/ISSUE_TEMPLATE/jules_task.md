name: Jules Task
description: Small, testable change for Jules to implement
title: "[Jules] one-sentence goal"
labels: ["jules"]
body:
  - type: textarea
    id: context
    attributes:
      label: Context
      description: What code area and why now?
      placeholder: e.g., Upgrade Next.js to v15 in /web; fix breaking tests in checkout.
  - type: textarea
    id: constraints
    attributes:
      label: Constraints
      description: Perf budgets, style rules, API contracts that must not change.
      placeholder: TypeScript strict; no schema changes; Lighthouse >= 90.
  - type: textarea
    id: acceptance
    attributes:
      label: Acceptance tests
      description: Exact checks we will run
      placeholder: |
        - Unit: cart totals handle discounts and GST
        - E2E: checkout happy path; no 500s; CI green
