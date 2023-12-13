import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Heat Gain Calculator',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: HeatGainCalculator(),
    );
  }
}

class HeatGainCalculator extends StatefulWidget {
  @override
  _HeatGainCalculatorState createState() => _HeatGainCalculatorState();
}

class _HeatGainCalculatorState extends State<HeatGainCalculator> {
  double uValue = 0.0;
  double surfaceArea = 0.0;
  double initialCLTD = 0.0;
  double lm = 0.0;
  double tr = 0.0;
  double t0 = 0.0;
  double f = 0.0;
  double heatGain = 0.0;

  void calculateHeatGain() {
    double updatedCLTD =
    ((initialCLTD + lm) * f + (78 - tr) + (t0 - 85));

    setState(() {
      heatGain = uValue * surfaceArea * updatedCLTD;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Heat Gain Calculator'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter U Value (U)'),
              onChanged: (value) {
                setState(() {
                  uValue = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter Surface Area (A)'),
              onChanged: (value) {
                setState(() {
                  surfaceArea = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter Initial CLTD'),
              onChanged: (value) {
                setState(() {
                  initialCLTD = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter LM'),
              onChanged: (value) {
                setState(() {
                  lm = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter Tr'),
              onChanged: (value) {
                setState(() {
                  tr = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter T0'),
              onChanged: (value) {
                setState(() {
                  t0 = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            TextField(
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: 'Enter f'),
              onChanged: (value) {
                setState(() {
                  f = double.tryParse(value) ?? 0.0;
                });
              },
            ),
            SizedBox(height: 16.0),
            ElevatedButton(
              onPressed: calculateHeatGain,
              child: Text('Calculate Heat Gain'),
            ),
            SizedBox(height: 16.0),
            Text(
              'Heat Gain: $heatGain',
              style: TextStyle(fontSize: 20.0, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }
}
