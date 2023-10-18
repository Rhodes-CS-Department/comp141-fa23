test = {
  'name': 'game over tests',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from cs1.notebooks import *
          >>> reload_functions("tiger_time.py")
          >>> next_player("Nakal")
          'Suci'
          >>> next_player("Suci")
          'Nakal'
          """,
          'hidden': True,
          'locked': True,
        }
      ],
      'scored': False,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
